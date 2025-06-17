from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    price=models.IntegerField()
    language=models.CharField(max_length=100)
    pages=models.IntegerField()
    image=models.ImageField(upload_to='books/',default='books/x.jpg')

from django.db import models
from random import randint

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone=models.IntegerField()
    address=models.TextField()
    # role=models.CharField(max_length=20,default=" ")r
    is_verified=models.BooleanField(default=False)
    # otp=models.CharField(max_length=10,null=True,blank=True)