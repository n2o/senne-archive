from django.db import models
from django.utils import timezone


class CreatedModifiedModel(models.Model):
    created = models.DateTimeField("Hinzugefügt am", default=timezone.now)
    modified = models.DateTimeField("Zuletzt geändert", auto_now=True)

    class Meta:
        abstract = True
