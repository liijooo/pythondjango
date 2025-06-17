from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone=models.IntegerField()
    address=models.TextField()
