from PIL import Image as ImagePillow
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Image, Upload
from .serializers import UploadSerializer


class ImageViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    """
    A viewset that provides `create` and 'list' action
    """
    serializer_class = UploadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Upload.objects.filter(user=self.request.user)