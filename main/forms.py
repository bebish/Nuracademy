# forms.py
from django import forms
from .models import Video, CustomUser

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_file']


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'last_name', 'number', 'check_photo']