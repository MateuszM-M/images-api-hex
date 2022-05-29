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
    Create thumbnails.
    
    Parameters
    ----------
    name : takes name from image_upload to name thumbnails
    file_format : take file format from image_upload to add it to thumbnail name
    thumbnails : get user's tier thumbnails to be able to iterate through it
    thb_upload : creates copy of image_upload 
                 to be able to multiple resize through loop
    img_io : BytesIO object to save resized image in memory
    image : image from image_upload opened in pillow
    hegiht : states height from tier for resizing
    width : states image width after resize, based on height
    resized : pillow resized image
    new_img : instantiates InMemoryUploadedFile to change it in thb_upload
    """
    name = image_upload['image'].name.split('.')[0]
    file_format = image_upload['image'].name.split('.')[-1]
    
    thumbnails = tier.thumbnails.all()
    
    for t in thumbnails:
        thb_upload = image_upload
        img_io = BytesIO()
        image = ImagePillow.open(thb_upload['image'])
        height = t.max_height
        width = height * image.width // image.height
        resized = image.resize(
            (width, height), 
            ImagePillow.ANTIALIAS)
        resized.save(img_io, format=image.format)
        new_img = InMemoryUploadedFile(
            img_io,
            'ImageField',
            f"{name}_thumbnail_{t.max_height}px.{file_format}",
            image.format,
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
