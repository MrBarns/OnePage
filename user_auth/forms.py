from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, PasswordInput

from .models import *


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length = 128, widget= PasswordInput)

class detailsForm(ModelForm):
    class Meta:
        model = UserContactDetails
        fields = ("first_name", "last_name", "linkdin", "facebook_name", "twitter_name", "instagram")
