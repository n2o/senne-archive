from django.contrib import admin
from reversion.admin import VersionAdmin

from .models import Item, Author


@admin.register(Author)
class AuthorAdmin(VersionAdmin):
    list_display = ('lastname', 'firstname', 'title', 'filepath')
    list_filter = ['title', 'firstname', 'lastname']
    search_fields = ['title', 'firstname', 'lastname']
    save_as = True
    readonly_fields = ['created', 'modified', 'filepath']
    ordering = ('lastname',)

    fieldsets = [
        ('Titel und Verfasser',
         {'fields': [
             'title', 'firstname', 'lastname',
         ]}),
        ('Speicherpfad',
         {'fields': [
             ('filepath'),
         ]}),
        ('Meta-Informationen',
         {'fields': [
             ('created', 'modified'),
         ]}),
    ]


@admin.register(Item)
class ItemAdmin(VersionAdmin):
    list_display = ('title', 'author', 'medart', 'public', 'modified')
    list_filter = ['medart', 'source_date', 'author', 'public']
    search_fields = ['title', 'author', 'abstract']
    save_as = True
    readonly_fields = ['created', 'modified']
    ordering = ('-modified',)

    fieldsets = [
        ('Titel und Verfasser',
         {'fields': [
             'title',
             'author',
             'role'
         ]}),
        ('Quelle',
         {'fields': [
             'source_title', 'amount',
             'medart', 'location', 'owner',
             ('year', 'source_date', 'number'),
             ('pages', 'place'),
             'notes'
         ]}),
        ('Abstract',
         {'fields': [
             'abstract'
         ]}),
        ('Dateien',
         {'fields': [
             ('digital_reference'),
             ('file1', 'file2', 'file3'),
             ('image1', 'image2', 'image3'),
         ]}),
        ('Meta-Informationen',
         {'fields': [
             'public',
             ('created', 'modified'),
         ]}),
    ]
