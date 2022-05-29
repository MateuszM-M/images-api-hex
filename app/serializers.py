import sys
from io import BytesIO

from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image as ImagePillow
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Image, Upload


class ImageReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']
        
        
class ImageWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']
      
    def validate_image(self, value):
        img = ImagePillow.open(value)
        if img.format.lower() not in ['jpeg', 'jpg', 'png']:
            raise ValidationError(
                "Only .jpg and .png formats are allowed."
            )
        return super(ImageWriteSerializer, self).validate(value)
    

class UploadSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True, 
        default=serializers.CurrentUserDefault()
        )
    images = ImageReadSerializer(many=True, read_only=True)
    image_upload = ImageWriteSerializer(write_only=True)
    
    class Meta:
        model = Upload
        fields = ['user', 'images', 'image_upload']
        
    def create(self, validated_data):
        image_upload = validated_data.pop('image_upload')
        upload = Upload.objects.create(**validated_data)
        img_io = BytesIO()
        Image.objects.create(upload=upload, **image_upload)
        
        thumbnails = validated_data['user'].tier.thumbnails.all()
        for t in thumbnails:
            image = ImagePillow.open(image_upload['image'])
            thb = image.resize((t.max_height, t.max_height), ImagePillow.ANTIALIAS)
            thb.save(img_io, format=image.format)
            new_pic = InMemoryUploadedFile(
                img_io,
                'ImageField',
                f"{image_upload['image'].name}_thumbnail_{t.max_height}px.{image.format}",
                image.format,
                sys.getsizeof(img_io),
                None)
            
            image_upload['image'] = new_pic
            Image.objects.create(upload=upload, **image_upload)
            
        return upload
        
    def save(self, **kwargs):
        """
        Include default for read_only `user` field
        """
        kwargs["user"] = self.fields["user"].get_default()
        return super().save(**kwargs)
