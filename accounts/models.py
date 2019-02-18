from django.db.models.signals import post_save
from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=50, blank=True)
    contact = models.CharField(max_length=12)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        userprofile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)