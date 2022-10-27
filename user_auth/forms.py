from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import PasswordInput

from .models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length = 128, widget= PasswordInput)

class detailsForm(forms.Form):
    first_name = forms.CharField(max_length = 100)
    last_name = forms.CharField(max_length = 100)
    linkdin = forms.CharField(max_length = 300, required = False)
    facebook_name = forms.CharField(max_length = 300, required = False)
    twitter_name = forms.CharField(max_length = 300, required = False)
    instagram = forms.CharField(max_length = 300, required = False)