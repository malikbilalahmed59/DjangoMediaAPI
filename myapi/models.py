# models.py
from django.db import models
from django.contrib.auth.models import User, AbstractUser, Permission, Group

from ApiProject import settings
from myapi.managers import CustomUserManager


class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    byte = models.CharField(max_length=50,null=True)
    size = models.CharField(max_length=100,null=True)
    extention = models.CharField(max_length=100,null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)


class Video(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')
    byte = models.CharField(max_length=50,null=True)
    size = models.CharField(max_length=100,null=True)
    extention = models.CharField(max_length=100,null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
