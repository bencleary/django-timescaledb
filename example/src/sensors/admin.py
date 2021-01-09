from django.contrib import admin
from django.contrib.gis import admin as gisAdmin
from .models import Sensor

admin.site.register(Sensor, gisAdmin.GeoModelAdmin)
