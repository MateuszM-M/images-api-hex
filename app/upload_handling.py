import sys
from io import BytesIO

from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image as ImagePillow

from .models import Image


def create_original_image(tier, upload, image_upload):
    """
    Creates image instance of originally uploaded image
    if user's tier allows that.
    """
    
    if tier.is_original_allowed:
        Image.objects.create(upload=upload,
                            label="original_picture",
                            **image_upload)
    return upload


def create_thumbnails(tier, upload, image_upload):
    """
    Create thumbnails
    
    After hours, it still has bugs :(
    """
    img_io = BytesIO()
    
    restart_image = image_upload['image']
    thb_upload = image_upload
    
    thumbnails = tier.thumbnails.all()
    
    for t in thumbnails:
        thb_upload['image'] = restart_image
        image = ImagePillow.open(thb_upload['image'])
        resized = image.resize((t.max_height, t.max_height))
        resized.save(img_io, format=image.format)
        new_img = InMemoryUploadedFile(
            img_io,
            'ImageField',
            f"{image_upload['image'].name}_thumbnail_{t.max_height}px.{image.format}",
            f"(image/{image.format})",
            sys.getsizeof(img_io),
            None)
        
        thb_upload['image'] = new_img
        Image.objects.create(upload=upload,
                             label=f"thumbnail_{t.max_height}",
                             **thb_upload)
        
    return upload


def tier_based_image_create(tier, upload, image_upload):
    """ Called in serializer. Creates images in upload in elegant way,
    based on user's tier."""
    
    create_original_image(tier, upload, image_upload)
    
    create_thumbnails(tier, upload, image_upload)
    
    return upload
