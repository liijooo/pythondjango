from django import forms
from django.forms import PasswordInput, CharField, IntegerField


class MoviesForm(forms.Form):
    movie_name=CharField()
    description=CharField()
    director_name=CharField()
    year=IntegerField()
    languages=CharField()