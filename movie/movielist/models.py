from django.db import models

class Book(models.Model):
    movie_name=models.CharField(max_length=100)
    description=models.TextField(max_length=100)
    director_name=models.CharField(max_length=100)
    language=models.CharField(max_length=100)
    year=models.IntegerField()
