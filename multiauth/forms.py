from django.core import validators
from django import forms
from .models import Student, Teacher, User, UserProfileImage
from django.core.exceptions import ValidationError
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


class StudentSignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    student_id = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    dept = forms.CharField(required=True)
    university = forms.CharField(required=True)
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']

    def clean_student_id(self):
        student_id = self.cleaned_data.get('student_id')
        for instance in Student.objects.all():
            if instance.student_id == student_id:
                raise forms.ValidationError("Student ID should be unique.")
     
        return student_id

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.name = self.cleaned_data.get('name')
        student.student_id = self.cleaned_data.get('student_id')
        student.phone = self.cleaned_data.get('phone')
        student.dept = self.cleaned_data.get('dept')
        student.university = self.cleaned_data.get('university')
        student.save()
        return student






class StudentUpdateForm(forms.ModelForm):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    dept = forms.CharField(required=True)
    university = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ['name', 'phone', 'dept', 'university']
        exclude=['username', 'email', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        student = Student.objects.get(user=user)
        student.name = self.cleaned_data.get('name')
        student.phone = self.cleaned_data.get('phone')
        student.dept = self.cleaned_data.get('dept')
        student.university = self.cleaned_data.get('university')
        student.save()
        return student









class TeacherSignUpForm(UserCreationForm):
    designation = forms.CharField(required=True)
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    dept = forms.CharField(required=True)
    university = forms.CharField(required=True)
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.designation = self.cleaned_data.get('designation')
        teacher.name = self.cleaned_data.get('name')
        teacher.phone = self.cleaned_data.get('phone')
        teacher.dept = self.cleaned_data.get('dept')
        teacher.university = self.cleaned_data.get('university')
        teacher.save()
        return teacher





class TeacherUpdateForm(forms.ModelForm):
    designation = forms.CharField(required=True)
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    dept = forms.CharField(required=True)
    university = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ['name', 'designation', 'phone', 'dept', 'university']
        exclude=['username', 'email', 'password1', 'password2']
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        teacher = Teacher.objects.get(user=user)
        teacher.designation = self.cleaned_data.get('designation')
        teacher.name = self.cleaned_data.get('name')
        teacher.phone = self.cleaned_data.get('phone')
        teacher.dept = self.cleaned_data.get('dept')
        teacher.university = self.cleaned_data.get('university')
        teacher.save()
        return teacher


  

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileImage
        fields = ['image']

