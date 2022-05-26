from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Photo
from .serializers import PhotoSerializer


class PhotoViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    """
    A viewset that provides `create` and 'list' action
    """
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Photo.objects.filter(user=self.request.user)