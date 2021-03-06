from django import template

register = template.Library()


@register.filter(is_safe=True)
def or_blank(field):
    """
    Shows field if not empty

    :param field:
    :return:
    """
    if field:
        return field
    else:
        return ""


@register.filter(is_safe=True)
def or_blank_with_title(field, title):
    """
    Shows field if not empty

    :param field:
    :return:
    """
    if field:
        return "{}: {}<br>".format(title, field)
    else:
        return ""


@register.filter(is_safe=True)
def col_if_field_exists(field, name):
    if field:
        return """
            <div class='row'>
                <div class='col-2'>
                    {}
                </div>
                <div class='col-10'>
                    {}
                </div>
            </div>
        """.format(name, field)
    return ""


@register.filter(is_safe=True)
def heading_if_field_exists(field, name):
    if field:
        return "<h4>{}</h4><p>{}</p>".format(name, field)
    return ""


@register.filter(is_safe=True)
def paragraph_if_field_exists(field, name):
    if field:
        return "<p>{}: {}</p>".format(name, field)
    return ""


@register.filter(is_safe=True)
def extract_filename(file):
    splitted = file.split("/")[2:]
    return "/".join(splitted)


@register.filter(is_safe=True)
def get_extension(file):
    return file.split(".")[-1]


@register.filter(is_safe=True)
def fa_attachment(extension):
    """
    Add fontawesome icon if found. Else return normal extension as string.

    :param extension: file extension
    :return: matching fontawesome icon as string
    """
    if extension == 'pdf':
        return "<i class='fa fa-file-pdf-o'></i>"
    elif extension == 'jpg' or extension == 'png':
        return "<i class='fa fa-picture-o'></i>"
    elif extension == 'doc' or extension == 'docx':
        return "<i class='fa fa-file-word-o'></i>"
    elif extension == 'xls' or extension == 'xlsx':
        return "<i class='fa fa-file-excel-o'></i>"
    elif extension == 'extern':
        return "<i class='fa fa-external-link'></i>"
    elif extension == 'zip':
        return "<i class='fa fa-file-archive-o'></i>"
    else:
        return ""
