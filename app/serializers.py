from rest_framework import serializers

from .models import Photo, User


class UserSerialzier(serializers.ModelSerializer):
    class Meta:
        model = User


class PhotoSerializer(serializers.ModelSerializer):
    user = UserSerialzier
    class Meta:
        model = Photo
        fields = ['user', 'photo']
