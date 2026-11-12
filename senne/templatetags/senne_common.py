import os

import markdown as md
import nh3
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def markdown(text):
    # Staff-authored, but not every staff account is a superuser: strip scripts/handlers/js: links.
    return mark_safe(nh3.clean(md.markdown(text or "", extensions=["extra", "sane_lists"])))


@register.filter
def extract_filename(file):
    return file.rsplit("/", 1)[-1]


@register.filter
def file_kind(name):
    """'archive/x/Bericht.pdf' -> 'PDF'; the stamp on a voucher sheet."""
    ext = os.path.splitext(name)[1][1:]
    return ext.upper() if ext.isalnum() and len(ext) <= 4 else "Datei"


@register.filter
def tilt(pk):
    """Stamps sit a little askew, each sheet its own way (-2deg … 2deg)."""
    return f"{pk * 7 % 5 - 2}deg"
