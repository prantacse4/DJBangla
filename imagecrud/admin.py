from django.contrib import admin
from .models import ImageDatabase
# Register your models here.

@admin.register(ImageDatabase)
class ImageDatabaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'date')
