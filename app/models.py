from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import validate_max_height


class Tier(models.Model):
    name = models.CharField(max_length=15)
    
    
class Thumbnail(models.Model):
    max_heigh = models.PositiveIntegerField(
        validators=[validate_max_height]
    )
    tier = models.ForeignKey(Tier,
                             related_name='thumbnails',
                             on_delete=models.CASCADE)


class User(AbstractUser):
    tier = models.OneToOneField(Tier, 
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True)
    

class Upload(models.Model):
    user = models.ForeignKey(User,
                             related_name='upload',
                             on_delete=models.CASCADE)


class Image(models.Model):
    upload = models.ForeignKey(Upload,
                               related_name='images',
                               on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")
    