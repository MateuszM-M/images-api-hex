from rest_framework import mixins, viewsets

from .models import Photo
from .serializers import PhotoSerializer


class PhotoViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    """
    A viewset that provides `create` action
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

