from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length = 100, unique = True)
    email = models.EmailField(unique=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class UserContactDetails(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    linkdin = models.CharField(max_length = 300, blank = True)
    facebook_name = models.CharField(max_length = 300, blank = True)
    twitter_name = models.CharField(max_length = 300, blank = True)
    instagram = models.CharField(max_length = 300, blank = True)

