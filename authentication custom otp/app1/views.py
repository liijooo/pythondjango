from django.shortcuts import render,redirect


from django.views import View
from app1.forms import SignupForm
from django.contrib import messages
class IndexView(View):
    def get(self,request):
        return render(request,'home.html')

class StudentHomeView(View):
    def get(self,request):
        return render(request,'student.html')


class TeacherHomeView(View):
    def get(self,request):
        return render(request,'teacher.html')


class AdminHomeView(View):
    def get(self,request):
        return render(request,'admin.html')


from django.core.mail import send_mail
class SignupView(View):
    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            user=form_instance.save(commit=False)# user represents model instance created
            user.is_active=False
            user.save()
            user.generate_otp()
            send_mail(
                "Django auth otp",
                user.otp,
                "tlijo979@gmail.com",
                [user.email],
                fail_silently=False,
            )
            return redirect('verify')


    def get(self,request):
        form_instance=SignupForm()
        return render(request,'signup.html',{'form':form_instance})

from app1.forms import LoginForm
from django.contrib.auth import authenticate,login
class SigninView(View):
    def post(self,request):
        form_instance=LoginForm(request.POST)
        if form_instance.is_valid():
            name=form_instance.cleaned_data['username']
            pswd=form_instance.cleaned_data['password']
            user=authenticate(username=name,password=pswd)
            if user and user.is_superuser==True:
                login(request,user)
                return redirect('admin')
            elif user and user.role=='student':
                login(request,user)
                return redirect('student')
            elif user and user.role=='teacher':
                login(request,user)
                return redirect('teacher')
            else:
                print('invalid user credentials')


            
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


from app1.models import User
class OtpverificationView(View):
    def post(self,request):
        otp=request.POST.get('otp')
        print(otp)
        try:
            u=User.objects.get(otp=otp)
            u.is_active=True
            u.is_verified=True
            u.otp=None
            u.save()
            return redirect('signin')
        except:
            # print('invalid otp')
            messages.error(request,'invalid otp')
            return redirect('verify')

    def get(self,request):
        return render(request,'verify.html')




