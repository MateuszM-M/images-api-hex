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
        return super(PhotoSerializer, self).validate(value)


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
        Image.objects.create(upload=upload, **image_upload)
        return upload
        
    def save(self, **kwargs):
        """
        Include default for read_only `user` field
        """
        kwargs["user"] = self.fields["user"].get_default()
        return super().save(**kwargs)
