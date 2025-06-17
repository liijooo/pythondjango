from django.shortcuts import render,redirect

def home(request):
    return render(request,'home.html')
from books.models import Book
def addbook(request):
    if(request.method=='POST'):
        print(request.POST)
        print(request.FILES)
        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        l=request.POST['l']
        g=request.POST['g']
        i=request.POST['i']

        b=Book.objects.create(title=t,author=a,price=p,language=l,pages=g,image=i)
        b.save()
        return redirect('books:viewbook')
    return render(request,'addbook.html')

from books.forms import BookForm
def addbook1(request):
    if(request.method=='POST'):
        print(request.POST)
        print(request.FILES)
        form_instance=BookForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()

        return redirect('books:viewbook')
    if(request.method=='GET'):
        form_instance=BookForm()
        return render(request,'addbook1.html',{'form':form_instance})

def viewbook(request):
    b=Book.objects.all()
    print(b)
    return render(request,'viewbook.html',{'books':b})


def bookdetail(request,i):
    b=Book.objects.get(id=i)
    return render(request,'detail.html',{'book':b})


def editbook(request,i):
    b = Book.objects.get(id=i)
    if(request.method=='POST'):
        form_instance=BookForm(request.POST,request.FILES,instance=b)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('books:viewbook')


    form_instance=BookForm(instance=b)
    return render(request,'editbook.html',{'form':form_instance})


def deletebook(request,i):
    b=Book.objects.get(id=i)
    b.delete()
    return redirect('books:viewbook')

from django.db.models import Q
def searchbook(request):
    if(request.method=='POST'):
        data=request.POST['q']
        print(data)
        b=Book.objects.filter(Q(title__contains=data) | Q(author__contains=data) | Q(language__contains=data))
        print(b)
        context={'book':b}
        return render(request,'search.html',context)
    return render(request,'search.html')