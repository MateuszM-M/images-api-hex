from django.contrib import admin

from .models import Thumbnail, Tier, User, Upload


class UserAdmin(admin.ModelAdmin):
    model = User
    
    
class ThumbnailInline(admin.StackedInline):
    model = Thumbnail
    
    
class TierAdmin(admin.ModelAdmin):
    model = Tier
    inlines = [ThumbnailInline]

admin.site.register(User, UserAdmin)
admin.site.register(Tier, TierAdmin)
admin.site.register(Upload)