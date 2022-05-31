from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from .validators import (validate_max_duration, validate_max_height,
                         validate_min_duration)


class Tier(models.Model):
    """
    DB model to represent tier attibutes.
    
    Related to thumbnail model, so multiple custom thumbnail sizes
    can be added to a tier.
    
    Attributes
    ---------
    name : name of the tier
    is_original_allowed : if true, uploads image of original size
    is_expiring_allowed : if true, user can set upload expire time
    """
    name = models.CharField(
        max_length=15,
        verbose_name = "Tier name"
        )
    is_original_allowed = models.BooleanField(
        verbose_name = "Is uploading of original picture allowed?"
    )
    is_expiring_allowed = models.BooleanField(
        verbose_name = "Is setting expire time allowed?"
    )
    
    def __str__(self):
        return self.name
    
    
class Thumbnail(models.Model):
    """
    DB model to represent thumbnail attributes.
    
    Related to tier, so multiple custom thumbnail sizes
    can be added to a tier
    
    Attributes
    ---------
    max_height : describes max height of thumbnail in pixels,
                 between 0 and 1000 which is set in validator
    tier : relation with tier
    """
    max_height = models.PositiveIntegerField(
        validators=[validate_max_height]
    )
    tier = models.ForeignKey(
        Tier,
        related_name='thumbnails',
        on_delete=models.CASCADE
        )
    
    def __str__(self):
        return f"{self.tier}: max_height: {self.max_height}"
    
    class Meta:
        ordering = ['-max_height']


class User(AbstractUser):
    """
    DB model to add attributes that extend django user model.
    
    Attributes
    ---------
    tier : one tier can be set to many users, states user tier
    """
    tier = models.ForeignKey(
        Tier, 
        on_delete=models.SET_DEFAULT,
        default=1
        )


class Upload(models.Model):
    """
    DB model to represent uploads.
    
    Since purpose of the app is to upload same image multiple times
    with different sizes, upload object will be created when user
    uploads file. Original image and created thumbnail will be related 
    image instances to this object. Upload object with related images
    will be able to view in api endpoints.
    
    Related to user, so one user can have many uploads.
    Related to image, so one upload can consist of many images.
    
    Attributes
    ---------
    user : foreign key, one user can have many uploads
    created : object creation time
    duration : seconds added to created to set expire_date
    epxire_date : states when upload expires, created + duration
    """
    user = models.ForeignKey(
        User,
        related_name='upload',
        on_delete=models.CASCADE
        )
    created = models.DateTimeField(
        auto_now_add=True
        )
    duration = models.PositiveIntegerField(
        validators=[
            validate_max_duration,
            validate_min_duration],
        blank=True,
        null=True
        )
    expire_date = models.DateTimeField(
        blank=True,
        null=True
        )
    
    def __str__(self):
        return f"{self.id}, {self.user}"
    

class Image(models.Model):
    """
    DB model to represent image.
    
    Image object can be either original image or thumbnail.
    
    Attributes
    ---------
    upload : foreign key, on upload can consist of many images
    label : informs about image type, original or thumbnail
    image : actual image or thumbnail
    """
    upload = models.ForeignKey(
        Upload,
        related_name='images',
        on_delete=models.CASCADE
        )
    label = models.CharField(
        max_length=50
        )
    image = models.ImageField(
        upload_to="images"
        )
    
    def __str__(self):
        return f"{self.upload}, {self.label}, {self.image}"
    