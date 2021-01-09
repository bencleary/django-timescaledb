from django.db import models
from django.contrib.gis.db import models as gis


class Sensor(models.Model):
    name = models.CharField(max_length=255)
    station_ref = models.IntegerField()
    river = models.ForeignKey('rivers.River', on_delete=models.CASCADE)
    point = gis.PointField()

    def __str__(self):
        return self.name

