from django import forms
from django.forms import ModelForm
from .models import *


class PostForm(ModelForm):
   class Meta:
       model = Post
       exclude=['user']

class ForumPost_Form(ModelForm):
    class Meta:
        model=Forum
        exclude=['user']

class Resource_Form(ModelForm):
    class Meta:
        model=Resources
        exclude=['user']

class UserProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    class Meta:
        model = User_Profile
        fields = ['image']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['username'].initial = user.username 
    def save(self, commit=True):
        user_profile = super().save(commit=False)
        if commit:
            user_profile.save()
            user = user_profile.user
            user.username = self.cleaned_data['username']
            user.save()
        return user_profile