from django.core import validators
from django import forms
from .models import ImageDatabase
from django.core.exceptions import ValidationError


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageDatabase
        fields = ['image']