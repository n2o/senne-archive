from django.contrib import admin
from reversion.admin import VersionAdmin

from .models import DATED, Author, Item


class TypoYearFilter(admin.SimpleListFilter):
    """Finds years outside 1000–2100 (typos such as 19855); they show as "ohne Jahr" on the site."""

    title = "Jahr"
    parameter_name = "jahr"

    def lookups(self, request, model_admin):
        return [("unplausibel", "unplausibel (Tippfehler)")]

    def queryset(self, request, queryset):
        if self.value() == "unplausibel":
            return queryset.filter(~DATED, year__isnull=False)
        return queryset


@admin.register(Author)
class AuthorAdmin(VersionAdmin):
    list_display = ("lastname", "firstname", "title", "filepath")
    list_filter = ["title", "firstname", "lastname"]
    search_fields = ["title", "firstname", "lastname"]
    save_as = True
    readonly_fields = ["created", "modified", "filepath"]
    ordering = ("lastname",)

    fieldsets = [
        (
            "Titel und Verfasser",
            {
                "fields": [
                    "title",
                    "firstname",
                    "lastname",
                ]
            },
        ),
        (
            "Speicherpfad",
            {
                "fields": [
                    ("filepath"),
                ]
            },
        ),
        (
            "Meta-Informationen",
            {
                "fields": [
                    ("created", "modified"),
                ]
            },
        ),
    ]


@admin.register(Item)
class ItemAdmin(VersionAdmin):
    list_display = ("title", "author", "medart", "public", "modified")
    list_filter = [TypoYearFilter, "medart", "year", "author", "public"]
    search_fields = ["title", "author__lastname", "abstract"]
    save_as = True
    readonly_fields = ["created", "modified"]
    ordering = ("-modified",)

    fieldsets = [
        (
            "Titel und Verfasser",
            {
                "fields": [
                    "title",
                    "author",
                ]
            },
        ),
        (
            "Quelle",
            {
                "fields": [
                    "source_title",
                    "amount",
                    "medart",
                    "location",
                    "year",
                    ("place", "pages"),
                    "notes",
                    "keywords",
                ]
            },
        ),
        ("Abstract", {"fields": ["abstract"]}),
        (
            "Dateien",
            {
                "fields": [
                    ("digital_reference"),
                    ("file1", "file2", "file3"),
                    ("image1", "image2", "image3"),
                ]
            },
        ),
        (
            "Meta-Informationen",
            {
                "fields": [
                    "public",
                    ("created", "modified"),
                ]
            },
        ),
    ]
