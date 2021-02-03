from django.contrib import admin
from .models import Student
from .models import Teacher
from .models import User
from .models import UserProfileImage

# Register your models here.

# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ( 'user', 'first_name', 'last_name', 'email')
admin.site.register(Student)
admin.site.register(User)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'designation')

@admin.register(UserProfileImage)
class UserProfileImageAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'image')