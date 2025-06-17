from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("Django")

def index(request):
    return HttpResponse("index page")
