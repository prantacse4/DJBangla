from django.core import validators
from django import forms
from .models import *
from django.core.exceptions import ValidationError


class AddPhotoForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = ['album', 'image']


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['album']

    def clean_album(self):
        album = self.cleaned_data.get('album')
        for instances in Album.objects.all():
            if instances.album == album:
                raise forms.ValidationError("Already Inserted! Try Another")
        return album