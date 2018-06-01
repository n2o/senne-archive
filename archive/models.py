# -*- coding: utf-8 -*-
"""
Migration script:

with open("export_v180318.csv", "r") as f:
    reader = csv.DictReader(f)
    data = [r for r in reader]

for d in data:
    abstract = d['abstract']
    medart = d['edit.source']
    notes = d['comments'] + " " + d['source.title'] + " " + d['statement_of_responsibility']
    file1 = d['digital_reference']
    weblink = d['weblink']
    year = d['search_year'] if d['search_year'] != "" else None
    number = d['source.volume'] if d['source.volume'] != "" else None
    title = d['title']
    author = d['author.name']
    item = Item.objects.create(abstract=abstract, medart=medart, notes=notes, file1=file1, digital_reference=weblink,
                               year=year, number=number, title=title, author=author)
"""

import os

from datetime import datetime

from django.db import models


def construct_file_path(instance, filename: str) -> str:
    """
    Construct directory structure based on the general path and the author.

    Returns upload_to/lastname, firstname/ when the author is written as "lastname, firstname".

    :param instance: Item object
    :param filename: original filename
    :return: Constructed path for file
    :rtype: str
    """
    from pprint import pprint
    pprint(instance)
    pprint(filename)
    return os.path.join("{}/{}/".format("archive", instance.author), filename)


class Item(models.Model):
    upload_to = "archive/"

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
    author = models.CharField("Verfasser", max_length=256, blank=False, null=False)
    role = models.CharField("Rolle", max_length=256, blank=True, null=True)

    # Quelle
    medart = models.CharField("Medienart *", max_length=256, choices=medart_choices, blank=False)
    source_title = models.CharField("Quelltitel", max_length=1024, blank=True, null=True)
    abstract = models.TextField("Abstract", blank=True, null=True)
    year = models.IntegerField("Jahrgang", default=datetime.now().year, blank=True, null=True)
    number = models.CharField("Nummer", max_length=256, blank=True, null=True)
    source_date = models.DateField("Veröffentlichungsdatum", blank=True, null=True)
    pages = models.CharField("Seiten", max_length=256, blank=True, null=True)
    notes = models.TextField("Anmerkungen", blank=True, null=True)
    place = models.CharField("Ort / Veröffentlichung", max_length=256, blank=True, null=True)

    keywords = models.TextField("Schlagworte *", default="", blank=True, max_length=1024, null=True)
    location = models.CharField("Standort (analoges Archiv)", max_length=256, blank=True, null=True)
    amount = models.IntegerField("Anzahl / Exemplare", default=1, blank=True, null=True)
    owner = models.CharField("Besitzer", max_length=256, blank=True, null=True)
    public = models.BooleanField("Veröffentlichen?", default=False)

    digital_reference = models.URLField("Digitalreferenz (URL)", blank=True, null=True)

    file1 = models.FileField("1. Datei", upload_to=construct_file_path, blank=True, null=True)
    file2 = models.FileField("2. Datei", upload_to=construct_file_path, blank=True, null=True)
    file3 = models.FileField("3. Datei", upload_to=construct_file_path, blank=True, null=True)

    image1 = models.ImageField("1. Abbildung", upload_to=construct_file_path, blank=True, null=True)
    image2 = models.ImageField("2. Abbildung", upload_to=construct_file_path, blank=True, null=True)
    image3 = models.ImageField("3. Abbildung", upload_to=construct_file_path, blank=True, null=True)

    created = models.DateTimeField("Hinzugefügt am", default=datetime.now)
    modified = models.DateTimeField("Zuletzt geändert", auto_now=True)

    def __str__(self):
        return str(self.title)
