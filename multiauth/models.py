from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=254)
    student_id = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=11)
    dept = models.CharField(max_length=150)
    university = models.CharField(max_length=150)



class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    name = models.CharField(max_length=254)
    designation = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    dept = models.CharField(max_length=150)
    university = models.CharField(max_length=150)



class UserProfileImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to="uploaded_image/user")