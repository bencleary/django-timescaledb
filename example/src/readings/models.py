from django.db import models
from timescale.db.models.base import TimescaleModel

from timescale.db import models as tsdb


class Quality(models.IntegerChoices):
    GOOD = 1
    ESTIMATED = 2
    SUSPECT = 3
    UNCHECKED = 4
    MISSING = 5


class Reading(TimescaleModel):
    flow = models.FloatField(default=0)
    quality = models.IntegerField(choices=Quality.choices, default=Quality.UNCHECKED)


class RadicalReadings(tsdb.TimescaleModel):
    value = models.FloatField(default=0.0)