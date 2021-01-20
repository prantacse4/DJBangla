from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField( max_length=50)
    student_id = models.CharField(max_length=50, unique = True)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.student_id

class Project(models.Model):
    student  = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=50, unique = True)
    project_details = models.TextField()
    project_status  = models.IntegerField(default = 0)