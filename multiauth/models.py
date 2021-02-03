from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # first_name  = models.CharField(max_length=100)
    # last_name  = models.CharField(max_length=100)
    # phone = models.CharField(max_length=11)
    # class_roll = models.CharField(max_length=50)
    # dept = models.CharField(max_length=100)
    # profile_image = models.ImageField(upload_to="uploaded_image/student")


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # first_name  = models.CharField(max_length=100)
    # last_name  = models.CharField(max_length=100)
    # phone = models.CharField(max_length=11)
    # email = models.EmailField(max_length=254)
    designation = models.CharField(max_length=100)
    # dept = models.CharField(max_length=100)
    # profile_image = models.ImageField(upload_to="uploaded_image/teacher")


class UserProfileImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to="uploaded_image/user")