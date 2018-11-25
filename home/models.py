from django.contrib.gis.db import models

# Create your models here.
class Sensors_Data(models.Model):
    temp = models.IntegerField()
    IMU = models.IntegerField()
    latitude = models.IntegerField()
    longitude = models. IntegerField()
    location = models.PointField(u"longitude/latitude", geography=True, blank=True, null=True)

    class Meta:
        db_table = "test_1"