from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.db import models
from pagedown.widgets import AdminPagedownWidget


class PageDownAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {"widget": AdminPagedownWidget}}


admin.site.unregister(FlatPage)


@admin.register(FlatPage)
class PageAdmin(PageDownAdmin, FlatPageAdmin):
    """Impressum, Datenschutz etc. with the Markdown editor."""

    # Comments, login-only pages and custom templates are unused (columns keep their defaults);
    # one Site only, so no sites filter.
    fieldsets = ((None, {"fields": ("url", "title", "content", "sites")}),)
    list_filter = ()
