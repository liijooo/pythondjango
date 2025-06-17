from django import forms
from django.contrib.admindocs.views import user_has_model_view_permission

from django.contrib.auth.models import User
from django.forms import CharField

from django.contrib.auth.forms import UserCreationForm
class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2','email','first_name','last_name']

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
