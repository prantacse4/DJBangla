from django.contrib import admin
from .models import Album, Photos
# Register your models here.

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'album')

@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ('album', 'image')