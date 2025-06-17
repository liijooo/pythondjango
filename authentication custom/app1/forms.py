from django import forms
from django.contrib.admindocs.views import user_has_model_view_permission


from django.forms import CharField
from app1.models import User
from django.contrib.auth.forms import UserCreationForm
class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2','email','first_name','last_name','phone','address']

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
