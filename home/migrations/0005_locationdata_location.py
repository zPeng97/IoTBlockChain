# Generated by Django 2.1.2 on 2019-01-27 12:23

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_locationdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationdata',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326, verbose_name='longitude/latitude'),
        ),
    ]
