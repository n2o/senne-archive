from django.db import models

from senne.models import CreatedModifiedModel


class Frontpage(CreatedModifiedModel):
    image1_leading = models.ImageField("Bild Startseite links groß", upload_to="frontpage/", blank=False, null=True)
    image2_leading = models.ImageField("Bild Startseite oben rechts klein", upload_to="frontpage/", blank=False,
                                       null=True)
    image3_leading = models.ImageField("Bild Startseite unten rechts klein", upload_to="frontpage/", blank=False,
                                       null=True)

    block1_title = models.CharField("Block 1 Überschrift", max_length=256, blank=False)
    block1_subtitle = models.CharField("Block 1 Überschrift 2", max_length=256, blank=False)
    block1_content = models.TextField("Block 1 Inhalt", blank=False)
    block1_image = models.ImageField("Block 1 Bild", upload_to="frontpage/", blank=False)

    block2_title = models.CharField("Block 2 Überschrift", max_length=256, blank=True)
    block2_subtitle = models.CharField("Block 2 Überschrift 2", max_length=256, blank=True)
    block2_content = models.TextField("Block 2 Inhalt", blank=True)
    block2_image = models.ImageField("Block 2 Bild", upload_to="frontpage/", blank=True)

    block3_title = models.CharField("Block 3 Überschrift", max_length=256, blank=True)
    block3_subtitle = models.CharField("Block 3 Überschrift 2", max_length=256, blank=True)
    block3_content = models.TextField("Block 3 Inhalt", blank=True)
    block3_image = models.ImageField("Block 3 Bild", upload_to="frontpage/", blank=True)

    def __str__(self):
        return "Startseite"

    class Meta:
        verbose_name = 'Startseite'
        verbose_name_plural = 'Startseiten'
