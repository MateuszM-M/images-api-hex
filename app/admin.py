from django.contrib import admin

from .models import Image, Thumbnail, Tier, Upload, User


class UserAdmin(admin.ModelAdmin):
    """
    Lists users in admin.
    """
    model = User
    
    
class ThumbnailInline(admin.StackedInline):
    """
    Inline to list and create thumbnails in tier admin panel.
    """
    model = Thumbnail
    
    
class TierAdmin(admin.ModelAdmin):
    """
    Tier admin panel, includes thumbnail inline, so when creating
    tier custom thumnail sizes can be added
    """
    model = Tier
    inlines = [ThumbnailInline]
    
    
class ImageInline(admin.StackedInline):
    """
    Inline to list image in upload admin panel.
    """
    model = Image
    

class UploadAdmin(admin.ModelAdmin):
    """
    Upload admin panel, includes image inline.
    """
    model = Upload
    inlines = [ImageInline]
        

admin.site.register(User, UserAdmin)
admin.site.register(Tier, TierAdmin)
admin.site.register(Upload, UploadAdmin)
