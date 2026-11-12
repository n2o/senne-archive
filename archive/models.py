import os

from django.db import models
from django.db.models import CASCADE
from django.utils import timezone
from django.utils.text import slugify

from senne.models import CreatedModifiedModel


def construct_file_path(instance, filename: str) -> str:
    """archive/<author slug>/<filename>, or archive/ohne-autor/<filename> without an author."""
    author_dir = instance.author.filepath if instance.author else "ohne-autor"
    return os.path.join("archive", author_dir, filename)


def current_year() -> int:
    return timezone.now().year


def slugify_author(lastname: str, firstname: str | None = None, title: str | None = None) -> str:
    return slugify(replace_umlauts(format_author_name(firstname, lastname, title)))


def format_author_name(firstname: str, lastname: str, title: str):
    if not firstname:
        return lastname
    if title:
        return f"{lastname}, {title} {firstname}"
    return f"{lastname}, {firstname}"


def replace_umlauts(input: str):
    replacements = [("ß", "ss"), ("ü", "ue"), ("ä", "ae"), ("ö", "oe"), ("Ü", "Ue"), ("Ä", "Ae"), ("Ö", "Oe")]
    for s, r in replacements:
        input = input.replace(s, r)
    return input


class Item(CreatedModifiedModel):
    medart_choices = (
        ("Artikel", "Artikel"),
        ("Audiodatei", "Audiodatei"),
        ("Buch", "Buch"),
        ("CD / DVD", "CD / DVD"),
        ("Dia(s)", "Dia(s)"),
        ("Filmspule", "Filmspule"),
        ("Foto(s)", "Foto(s)"),
        ("Gegenstand", "Gegenstand"),
        ("Kassette", "Kassette"),
        ("Schallplatte", "Schallplatte"),
        ("Schrifttum", "Schrifttum"),
        ("Sonstiges", "Sonstiges"),
        ("Stempel", "Stempel"),
        ("Tonband", "Tonband"),
        ("VHS", "VHS"),
        ("Videodatei", "Videodatei"),
    )
    # Titel und Verfasser
    title = models.CharField("Titel *", max_length=1024, blank=False, null=False)
    author = models.ForeignKey("Author", on_delete=CASCADE, blank=False, null=True)

    # Quelle
    medart = models.CharField("Medienart *", max_length=256, choices=medart_choices, blank=False)
    source_title = models.CharField("Quelltitel", max_length=1024, blank=True, null=True)
    abstract = models.TextField("Abstract", blank=True, null=True)
    year = models.IntegerField("Jahrgang", default=current_year, blank=True, null=True)
    pages = models.CharField("Seiten", max_length=256, blank=True, null=True)
    notes = models.TextField("Anmerkungen", blank=True, null=True)
    place = models.CharField("Ort / Veröffentlichung", max_length=256, blank=True, null=True)

    keywords = models.TextField("Schlagworte", default="", blank=True, max_length=1024, null=True)
    location = models.CharField("Standort (analoges Archiv)", max_length=256, blank=True, null=True)
    amount = models.IntegerField("Anzahl / Exemplare", default=1, blank=True, null=True)
    public = models.BooleanField("Veröffentlichen?", default=True)

    digital_reference = models.URLField("Digitalreferenz (URL)", blank=True, null=True)

    file1 = models.FileField("1. Datei", upload_to=construct_file_path, max_length=255, blank=True, null=True)
    file2 = models.FileField("2. Datei", upload_to=construct_file_path, max_length=255, blank=True, null=True)
    file3 = models.FileField("3. Datei", upload_to=construct_file_path, max_length=255, blank=True, null=True)

    image1 = models.ImageField("1. Abbildung", upload_to=construct_file_path, max_length=255, blank=True, null=True)
    image2 = models.ImageField("2. Abbildung", upload_to=construct_file_path, max_length=255, blank=True, null=True)
    image3 = models.ImageField("3. Abbildung", upload_to=construct_file_path, max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.title)

    FILE_FIELDS = ("file1", "file2", "file3")
    IMAGE_FIELDS = ("image1", "image2", "image3")

    @property
    def files(self):
        return [f for f in (getattr(self, n) for n in self.FILE_FIELDS) if f]

    @property
    def images(self):
        return [i for i in (getattr(self, n) for n in self.IMAGE_FIELDS) if i]

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"


class Author(CreatedModifiedModel):
    title = models.CharField("Titel", max_length=256, blank=True, null=True)
    firstname = models.CharField("Vorname", max_length=256, blank=True, null=True)
    lastname = models.CharField("Nachname *", max_length=256, blank=False, null=False)
    filepath = models.SlugField(
        "Pfad wo die Dateien abgelegt werden (wird automatisch berechnet beim Speichern)",
        max_length=255,
        blank=True,
        null=True,
        unique=True,
    )

    def __str__(self):
        return format_author_name(self.firstname, self.lastname, self.title)

    def save(self, *args, **kwargs):
        if not self.filepath:
            self.filepath = slugify_author(self.lastname, self.firstname, self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autoren"
