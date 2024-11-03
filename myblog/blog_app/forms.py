# blog/forms.py

from django import forms
from django.contrib.auth.models import User
from .models import Page, Message, Profile
from django.contrib.auth.forms import UserCreationForm

class UserSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['description', 'image_url', 'website_url']

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'content']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'content']
