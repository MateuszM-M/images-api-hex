from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Image, Upload
from .serializers import UploadSerializer, UploadSerializerWithExpire

from django.utils import timezone
from django.db.models import Q


class UploadViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    """
    A viewset that provides `create` and 'list' action for upload.
    
    Restricted to authenticated users. 
    User can view only own upload.
    """
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Returns queryset of user's uploads that are not expired."""
        user = self.request.user
        tz = timezone.now()
        qs = Upload.objects.filter(user=user).filter(
            Q(expire_date__gt=tz) | Q(expire_date__isnull=True))
        return qs

    def get_serializer_class(self):
        """Returns serializer based on user tier"""
        user = self.request.user
        expire_allowed = user.tier.is_expiring_allowed
        if expire_allowed:
            return UploadSerializerWithExpire
        return UploadSerializer