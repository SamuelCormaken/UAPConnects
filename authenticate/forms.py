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