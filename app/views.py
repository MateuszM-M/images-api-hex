from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Image, Upload
from .serializers import UploadSerializer


class UploadViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    """
    A viewset that provides `create` and 'list' action for upload.
    
    Restricted to authenticated users. 
    User can view only own upload.
    """
    serializer_class = UploadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Upload.objects.filter(user=self.request.user)
