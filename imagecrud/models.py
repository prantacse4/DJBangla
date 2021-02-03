from django.db import models

# Create your models here.


class ImageDatabase(models.Model):
    image = models.ImageField(upload_to="uploaded_image")
    date = models.DateTimeField(auto_now_add=True)
    

