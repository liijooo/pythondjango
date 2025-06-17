from django.shortcuts import render

def home(request):
    context={'name':"arun",'age':22}
    return render(request,'home.html',context)

def first(request):
    return render(request,"first.html")

def second(request):
    return render(request,"second.html")
