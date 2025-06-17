from django import forms
from django.forms import PasswordInput, CharField, IntegerField


class AdditionForm(forms.Form):
    number1=forms.IntegerField()
    number2=forms.IntegerField()


class FactorialForm(forms.Form):
    number=forms.IntegerField()


class BmiForm(forms.Form):
    weight=forms.IntegerField()
    height=forms.IntegerField()


class SignupForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=50,widget=PasswordInput)
    email=forms.CharField()
    gender_choices=[('male','Male'),('female','Female')]
    gender=forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)
    role_choices=[('admin','Admin'),('student','Student')]
    role=forms.ChoiceField(choices=role_choices)


class CalculatorForm(forms.Form):
    gender_choices=[('male','Male'),('female','Female')]
    gender=forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)
    weight=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    height=forms.IntegerField()
    age=forms.IntegerField()
    ActivityLevel_choices=[(1.2,'Sedentary'),(1.375,'Lightly active'),(1.55,'Moderately active'),(1.725,'Very active'),(1.9,'Extra active')]
    ActivityLevel=forms.ChoiceField(choices=ActivityLevel_choices)

class AddbookForm(forms.Form):
    title=CharField()
    author=CharField()
    price=IntegerField()
    pages=IntegerField()
    languages=CharField()