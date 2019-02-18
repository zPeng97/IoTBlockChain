from django.db.models.signals import post_save
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class SensorsData(models.Model):
    temp = models.FloatField()
    IMU = models.FloatField()
    latitude = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(90.0)])
    longitude = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(180.0)])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    location = models.PointField(u"longitude/latitude", geography=True, blank=True, null=True)

    class Meta:
        db_table = "test_1"

class LocationData(models.Model):
    lat = models.FloatField('LATITUDE', validators=[MinValueValidator(0.0), MaxValueValidator(90.0)])
    long = models.FloatField('LONGITUDE', validators=[MinValueValidator(0.0), MaxValueValidator(180.0)])
    location = models.PointField(u"longitude/latitude", geography=True, blank=True, null=True)

    def __str__(self):
        return str(self.lat) + ',' + str(self.long)

    class Meta:
        db_table = "Location"


