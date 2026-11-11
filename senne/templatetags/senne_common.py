import markdown as md
from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe

register = template.Library()

ICONS = {
    "pdf": "fa-file-pdf-o",
    "jpg": "fa-picture-o",
    "jpeg": "fa-picture-o",
    "png": "fa-picture-o",
    "doc": "fa-file-word-o",
    "docx": "fa-file-word-o",
    "xls": "fa-file-excel-o",
    "xlsx": "fa-file-excel-o",
    "zip": "fa-file-archive-o",
}


@register.filter
def markdown(text):
    # Only staff edits these fields in the admin, so raw HTML stays allowed (as before).
    return mark_safe(md.markdown(text or "", extensions=["extra", "sane_lists"]))


@register.filter
def or_blank_with_title(field, title):
    if field:
        return format_html("{}: {}<br>", title, field)
    return ""


@register.filter
def heading_if_field_exists(field, name):
    if field:
        return format_html("<h2 class='h4'>{}</h2><p>{}</p>", name, field)
    return ""


@register.filter
def paragraph_if_field_exists(field, name):
    if field:
        return format_html("<p>{}: {}</p>", name, field)
    return ""


@register.filter
def extract_filename(file):
    return file.rsplit("/", 1)[-1]


@register.filter
def fa_attachment(filename):
    """Decorative Font Awesome icon for a file name, hidden from screen readers."""
    icon = ICONS.get(filename.rsplit(".", 1)[-1].lower())
    if icon:
        return format_html("<i class='fa {}' aria-hidden='true'></i>", icon)
    return ""
