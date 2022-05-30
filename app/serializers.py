from PIL import Image as ImagePillow
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from.upload_handling import tier_based_image_create
from .models import Image, Upload

from django.utils import timezone


class ImageReadSerializer(serializers.ModelSerializer):
    """Image serializer used on read in upload serializer"""

    class Meta:
        model = Image
        fields = ['label', 'image']
        
        
class ImageWriteSerializer(serializers.ModelSerializer):
    """Image serializer used on write in upload serializer"""
    class Meta:
        model = Image
        fields = ['image']
      
    def validate_image(self, value):
        """Validates image extension, checks if its jpg or png"""
        img = ImagePillow.open(value)
        if img.format.lower() not in ['jpeg', 'jpg', 'png']:
            raise ValidationError("Only .jpg and .png formats are allowed.")
        return super(ImageWriteSerializer, self).validate(value)
    

class UploadSerializer(serializers.ModelSerializer):
    """
    Upload serializer used for writing and reading upload objects.
    
    Attributes
    ---------
    user : user that uploads
    images : based on image read serializer
    imageee_upload : based on image write serializer
    """
    user = serializers.PrimaryKeyRelatedField(
        read_only=True, 
        default=serializers.CurrentUserDefault()
        )
    images = ImageReadSerializer(many=True, read_only=True)
    image_upload = ImageWriteSerializer(write_only=True)
    
    class Meta:
        model = Upload
        fields = [
            'user',
            'images',
            'image_upload',
            'created',
            'duration',
            'expire_date',
            ]
        extra_kwargs = {
            'duration': {'write_only':True},
            'expire_date': {'read_only':True}
        }
        
    def create(self, validated_data):
        """Creates upload instance. Calls tier_based_image_create
        to create images in elegant way, based on tier """
        user = validated_data['user']
        tier = user.tier
        image_upload = validated_data.pop('image_upload')
        
        if validated_data['duration']:
            validated_data['expire_date'] = \
            timezone.now() + timezone.timedelta(
                seconds=validated_data['duration'])
            
        upload = Upload.objects.create(**validated_data)
        
        tier_based_image_create(tier, upload, image_upload)
        
        return upload
        
    def save(self, **kwargs):
        """
        Include default for read_only `user` field
        """
        kwargs["user"] = self.fields["user"].get_default()
        return super().save(**kwargs)
