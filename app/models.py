from django.contrib.auth.models import AbstractUser
from django.db import models


class Tier(models.Model):
    name = models.CharField(max_length=15)


class User(AbstractUser):
    tier = models.OneToOneField(Tier, 
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True)
    

class Photo(models.Model):
    user = models.ForeignKey(User,
                             related_name='photos',
                             on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="photos")
