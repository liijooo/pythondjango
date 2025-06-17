from django.shortcuts import render,redirect

# def home(request):
#     return render(request,'home.html')

from django.views import View
class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'home.html')

from books.models import Book
# def addbook(request):
class AddbookView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'addbook.html')

    def post(self,request,*args,**kwargs):
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
# def addbook1(request):
class AddbookView1(View):
    def post(self,request,*args,**kwargs):
        print(request.POST)
        print(request.FILES)
        form_instance=BookForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()

        return redirect('books:viewbook')

    def get(self,request,*args,**kwargs):
        form_instance=BookForm()
        return render(request,'addbook1.html',{'form':form_instance})

class Viewbook(View):
    def get(self,request,*args,**kwargs):
        b=Book.objects.all()
        print(b)
        return render(request,'viewbook.html',{'books':b})


class Bookdetail(View):
    def get(self,request,i):
        b=Book.objects.get(id=i)
        return render(request,'detail.html',{'book':b})


class Editbook(View):
    def get(self,request,i):
        b = Book.objects.get(id=i)
        form_instance=BookForm(instance=b)
        return render(request,'editbook.html',{'form':form_instance})

    def post(self,request,i):
        b = Book.objects.get(id=i)
        form_instance=BookForm(request.POST,request.FILES,instance=b)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('books:viewbook')


class Deletebook(View):
    def get(self,request,i):
        b=Book.objects.get(id=i)
        b.delete()
        return redirect('books:viewbook')

from django.db.models import Q
class Searchbook(View):
    def post(self,request):
        data=request.POST['q']
        print(data)
        b=Book.objects.filter(Q(title__contains=data) | Q(author__contains=data) | Q(language__contains=data))
        print(b)
        context={'book':b}
        return render(request,'search.html',context)


from django.core.mail import send_mail

from books.forms import SignupForm
class SignupView(View):
    def post(self, request):
        form_instance =SignupForm(request.POST)
        if form_instance.is_valid():
            # user = form_instance.save(commit=False)  # user represents model instance created
            # user.is_active = False
            # user.save()
            # user.generate_otp()
            # send_mail(
            #     "Django auth otp",
            #     user.otp,
            #     "tlijo979@gmail.com",
            #     [user.email],
            #     fail_silently=False,
            # )
            # return redirect('verify')
            form_instance.save()
            return redirect('home.html')

    def get(self, request):
        form_instance =SignupForm()
        return render(request, 'register.html', {'form': form_instance})


from books.forms import LoginForm
from django.contrib.auth import authenticate, login


class SigninView(View):
    def post(self, request):
        form_instance = LoginForm(request.POST)
        if form_instance.is_valid():
            name = form_instance.cleaned_data['username']
            pswd = form_instance.cleaned_data['password']
            user = authenticate(username=name, password=pswd)
            if user:
                # starting session using current user
                login(request, user)
                u = request.user
                print(u)
                print(u.username)
                print(u.email)
                print(u.first_name)
                return redirect('base')
            else:
                print('invalid user credentials')

                return redirect('login')
            # print(name,pswd)

    def get(self, request):
        form_instance = LoginForm()
        return render(request, 'login.html', {'form': form_instance})


from django.contrib.auth import logout


class SignoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')