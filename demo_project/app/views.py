from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("welcome to home")

def first(request):
    return HttpResponse("first page")

def second(request):
    return HttpResponse("second page")

