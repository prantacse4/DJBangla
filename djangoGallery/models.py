from django.db import models

# Create your models here.

class Album(models.Model):
    album = models.CharField(max_length=50)

    def __str__(self):
        return self.album

class Photos(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploaded_image")