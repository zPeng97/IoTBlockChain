from django.contrib.gis.db import models


# Create your models here.
class SensorsData(models.Model):
    temp = models.FloatField()
    IMU = models.FloatField()
    latitude = models.FloatField()
    longitude = models. FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    location = models.PointField(u"longitude/latitude", geography=True, blank=True, null=True)

    class Meta:
        db_table = "test_1"