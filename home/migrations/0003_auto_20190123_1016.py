# Generated by Django 2.1.2 on 2019-01-23 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
