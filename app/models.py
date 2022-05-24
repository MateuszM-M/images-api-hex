from django.contrib.auth.models import AbstractUser
from django.db import models


class Tier(models.Model):
    name = models.CharField(max_length=15)


class User(AbstractUser):
    tier = models.OneToOneField(Tier, 
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True)
