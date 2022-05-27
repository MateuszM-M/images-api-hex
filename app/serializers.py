from PIL import Image
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True, 
        default=serializers.CurrentUserDefault()
        )
    
    class Meta:
        model = Photo
        fields = ['user', 'photo']
        
    def validate_photo(self, photo):
        img = Image.open(photo)
        if img.format.lower() not in ['jpeg', 'jpg', 'png']:
            raise ValidationError(
                "Only .jpg and .png formats are allowed."
            )
        return super(PhotoSerializer, self).validate(photo)
            

    def save(self, **kwargs):
        """
        Include default for read_only `user` field
        """
        kwargs["user"] = self.fields["user"].get_default()
        return super().save(**kwargs)
