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
