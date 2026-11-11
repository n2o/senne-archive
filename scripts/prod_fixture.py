"""One-off: turn a `dumpdata` of the old SQLite site into a fixture for the new Postgres site.

    SECRET_KEY=x DATABASE_URL=sqlite:////path/to/old/db.sqlite3 uv run python manage.py dumpdata \
        --natural-foreign --natural-primary -e contenttypes -e auth.permission -e sessions -e thumbnail \
        -o prod-raw.json
    python3 scripts/prod_fixture.py prod-raw.json prod.json

What it changes:
- drops rows that point at apps that no longer exist (testy, old flatpages) and revisions left empty by that
- the custom `pages.page` model is now `django.contrib.flatpages` (its `image` field was never used)
- Markdown headings of flat pages start at h2 without skipping levels (the page title is the h1)
"""

import json
import re
import sys

APPS = {"admin", "auth", "contenttypes", "sites", "sessions", "flatpages", "archive", "frontpage", "reversion"}
HEADING = re.compile(r"(?m)^(#{1,6})(?=\s)")


def normalize_headings(text):
    levels = sorted({len(h) for h in HEADING.findall(text)})
    if not levels:
        return text
    rank = {level: i + 2 for i, level in enumerate(levels)}
    text = HEADING.sub(lambda m: "#" * rank[len(m.group(1))], text)
    # Headings before the first h2 would otherwise follow the h1 directly at h3.
    first_h2 = text.find("\n## ")
    if first_h2 > 0:
        text = HEADING.sub("##", text[:first_h2]) + text[first_h2:]
    return text


def convert(objects):
    for o in objects:
        ct = o["fields"].get("content_type")
        if ct == ["pages", "page"]:
            o["fields"]["content_type"] = ["flatpages", "flatpage"]
        if o["model"] == "pages.page":
            o["model"] = "flatpages.flatpage"
            o["fields"].pop("image", None)
            o["fields"]["content"] = normalize_headings(o["fields"]["content"])

    def dead(o):
        ct = o["fields"].get("content_type")
        return bool(ct) and ct[0] not in APPS

    kept_revisions = {o["fields"]["revision"] for o in objects if o["model"] == "reversion.version" and not dead(o)}
    return [
        o for o in objects
        if not dead(o) and not (o["model"] == "reversion.revision" and o["pk"] not in kept_revisions)
    ]


if __name__ == "__main__":
    assert normalize_headings("#### a\n## b\n#### c") == "## a\n## b\n### c"  # the Impressum case
    src, dst = sys.argv[1:3]
    objects = json.load(open(src))
    result = convert(objects)
    json.dump(result, open(dst, "w"))
    print(f"{len(objects)} -> {len(result)} objects")
