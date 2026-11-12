from django.contrib import admin
from reversion.admin import VersionAdmin

from frontpage.models import Frontpage
from senne.admin import PageDownAdmin


@admin.register(Frontpage)
class FrontpageAdmin(PageDownAdmin, VersionAdmin):
    readonly_fields = ["created", "modified"]
    fieldsets = [
        ("Bilder Startseite", {"fields": ["image1_leading", "image2_leading", "image3_leading"]}),
        ("Block 1", {"fields": ["block1_title", "block1_subtitle", "block1_content", "block1_image"]}),
        ("Block 2", {"fields": ["block2_title", "block2_subtitle", "block2_content", "block2_image"]}),
        ("Block 3", {"fields": ["block3_title", "block3_subtitle", "block3_content", "block3_image"]}),
        (
            "Meta-Informationen",
            {
                "fields": [
                    ("created", "modified"),
                ]
            },
        ),
    ]
