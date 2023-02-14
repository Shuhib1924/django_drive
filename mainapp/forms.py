from django import forms
from .models import Folder, File


class NewFolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ('name',)
