from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import PasswordInput, CharField, IntegerField


from books.models import Book
class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields="__all__"

from books.models import User
from django.contrib.auth.forms import UserCreationForm
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'phone', 'address']


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()