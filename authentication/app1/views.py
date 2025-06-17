from django.shortcuts import render,redirect


from django.views import View
from app1.forms import SignupForm

class IndexView(View):
    def get(self,request):
        return render(request,'home.html')

class SignupView(View):
    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            user=form_instance.save(commit=False)# user represents model instance created
            user.set_password(form_instance.cleaned_data['password'])
            user.save()
            return redirect('home')

    def get(self,request):
        form_instance=SignupForm()
        return render(request,'signup.html',{'form':form_instance})

from app1.forms import LoginForm
from django.contrib.auth import authenticate,login
class SigninView(View):
    def post(self,request):
        form_instance=LoginForm(request.POST)
        if form_instance.is_valid():
            # name=form_instance.cleaned_data['username']
            # pswd=form_instance.cleaned_data['password']
            # user=authenticate(username=name,password=pswd)
            # if user:
            #     #starting session using current user
            #     login(request,user)
            #     u=request.user
            #     print(u)
            #     print(u.username)
            #     print(u.email)
            #     print(u.first_name)
            #     return redirect('home')
            # else:
            #     print('invalid user credentials')


                return redirect('signin')
            # print(name,pswd)


    def get(self,request):
        form_instance=LoginForm()
        return render(request,'login.html',{'form':form_instance})
from django.contrib.auth import logout
class SignoutView(View):
    def get(self,request):
        logout(request)
        return redirect('signin')