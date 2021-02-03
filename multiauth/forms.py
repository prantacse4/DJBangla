from django.core import validators
from django import forms
from .models import Student, Teacher, User, UserProfileImage
from django.core.exceptions import ValidationError
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


class StudentSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields =[ 'first_name', 'last_name','username', 'email', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        return user


class TeacherSignUpForm(UserCreationForm):
    designation = forms.CharField(required=True)
    class Meta:
        model = User
        fields =[ 'first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.designation = self.cleaned_data.get('designation')
        teacher.save()
        return teacher


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileImage
        fields = ['image']


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields =[ 'first_name', 'last_name']

class TeacherUpdateForm(forms.ModelForm):
    designation = forms.CharField(required=True)
    class Meta:
        model = User
        fields =[ 'first_name', 'last_name']
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        teacher = Teacher.objects.get(user=user)
        teacher.designation = self.cleaned_data.get('designation')
        teacher.save()
        return teacher


  
