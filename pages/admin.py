from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from senne.admin import PageDownAdmin
from .forms import PageForm
from .models import Page


class PageAdmin(PageDownAdmin):
    form = PageForm
    fieldsets = (
        (None, {'fields': ('url', 'image', 'title', 'content', 'sites')}),
        (_('Advanced options'), {'classes': ('collapse',),
                                 'fields': ('enable_comments', 'registration_required', 'template_name')}),
    )
    list_display = ('url', 'title')
    list_filter = ('sites', 'enable_comments', 'registration_required')
    search_fields = ('url', 'title')


admin.site.register(Page, PageAdmin)
