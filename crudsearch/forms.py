from django.core import validators
from django import forms
from .models import Student, Project
from django.core.exceptions import ValidationError


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'student_id', 'phone']

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        for instances in Student.objects.all():
            if instances.phone == phone:
                raise forms.ValidationError("Already Inserted! Try Another")
        
        return phone


class ProjectRegistration(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['student', 'project_name', 'project_details']
