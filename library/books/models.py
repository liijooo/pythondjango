from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    price=models.IntegerField()
    language=models.CharField(max_length=100)
    pages=models.IntegerField()
    image=models.ImageField(upload_to='books/',default='books/x.jpg')