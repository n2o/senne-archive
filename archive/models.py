import os
from functools import cached_property

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import CASCADE, Case, Count, F, IntegerField, Q, Value, When
from django.utils import timezone
from django.utils.text import slugify

from senne.models import CreatedModifiedModel


def construct_file_path(instance, filename: str) -> str:
    """archive/<author slug>/<filename>, or archive/ohne-autor/<filename> without an author."""
    author_dir = instance.author.filepath if instance.author else "ohne-autor"
    return os.path.join("archive", author_dir, filename)


def current_year() -> int:
    return timezone.now().year


NO_YEAR = "ohne"
YEARS = (1000, 2100)  # anything outside is a typo in the data and counts as "ohne Jahr"
DATED = Q(year__gte=YEARS[0], year__lte=YEARS[1])


def decade_value(year: int | None) -> str:
    """1958 -> '1950', None or a typo like 19855 -> NO_YEAR; the value of the ?jahrzehnt= filter."""
    if year is None or not YEARS[0] <= year <= YEARS[1]:
        return NO_YEAR
    return str(year // 10 * 10)


def decade_label(value: str) -> str:
    """'1950' -> '1950er', NO_YEAR -> 'ohne Jahr'."""
    return "ohne Jahr" if value == NO_YEAR else f"{value}er"


class ItemQuerySet(models.QuerySet):
    def decades(self):
        """[(value, label, count)] in order, items without a year last; counted by the database."""
        decade = Case(When(DATED, then=F("year") / 10 * 10), output_field=IntegerField())
        rows = self.order_by().annotate(d=decade).values_list("d").annotate(n=Count("pk"))
        values = [(decade_value(d), n) for d, n in sorted(rows, key=lambda r: (r[0] is None, r[0] or 0))]
        return [(value, decade_label(value), n) for value, n in values]

    def in_decade(self, value):
        if value == NO_YEAR:
            return self.exclude(DATED)
        if value:
            return self.filter(DATED, year__gte=int(value), year__lt=int(value) + 10)
        return self

    def chronological(self):
        """Oldest first; items without a (plausible) year last."""
        undated = Case(When(DATED, then=Value(0)), default=Value(1))
        return self.order_by(undated, "year", "title", "pk")

    def medarts(self):
        """[(medart, count)], most frequent first."""
        return list(self.order_by().values_list("medart").annotate(n=Count("pk")).order_by("-n", "medart"))


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
    year = models.IntegerField(
        "Jahrgang",
        default=current_year,
        blank=True,
        null=True,
        validators=[MinValueValidator(YEARS[0]), MaxValueValidator(YEARS[1])],
    )
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

    objects = ItemQuerySet.as_manager()

    def __str__(self):
        return str(self.title)

    FILE_FIELDS = ("file1", "file2", "file3")
    IMAGE_FIELDS = ("image1", "image2", "image3")

    @cached_property
    def files(self):
        return [f for f in (getattr(self, n) for n in self.FILE_FIELDS) if f]

    @cached_property
    def images(self):
        return [i for i in (getattr(self, n) for n in self.IMAGE_FIELDS) if i]

    @property
    def number(self):
        """Inventory label shown on the archive's voucher sheets."""
        return f"SA-{self.pk:04d}"

    @property
    def dated_year(self):
        """The year, or None when it is missing or a typo outside YEARS."""
        return None if decade_value(self.year) == NO_YEAR else self.year

    @property
    def decade(self):
        return decade_label(decade_value(self.year))

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
