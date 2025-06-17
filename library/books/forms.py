from django import forms
from django.forms import PasswordInput, CharField, IntegerField


# class BookForm(forms.Form):
#     title=CharField(max_length=100)
#     author=CharField(max_length=100)
#     price=IntegerField()
#     pages=IntegerField()
#     languages=CharField(max_length=100)
#     image=forms.ImageField()


from books.models import Book
class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields="__all__"