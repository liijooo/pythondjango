from django.db import models

class movie(models.Model):
    Movie_Name=models.CharField(max_length=100)
    Description=models.CharField(max_length=100)
    Language=models.CharField()
    Year=models.IntegerField()
    Director_name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="movies")
