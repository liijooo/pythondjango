from django import forms
from movielist.models import movie
from django.forms import PasswordInput, CharField, IntegerField

#
# class MovieForm(forms.Form):
#     Movie_Name=CharField(max_length=100)
#     Description=CharField(max_length=100)
#     Language=CharField()
#     Year=IntegerField()
#     Director_name=CharField(max_length=100)
#     image=forms.ImageField()

class MovieForm(forms.ModelForm):
    class Meta:
        model=movie
        fields=['Movie_Name','Description','Director_name','Language','Year','image']