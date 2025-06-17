from django.shortcuts import render

from app1.forms import AdditionForm
def addition(request):
    if(request.method=='POST'):
        print(request.POST)
        return render(request,'addition.html')
    form_instance=AdditionForm()
    return render(request,'addition.html',{'form':form_instance})

from app1.forms import FactorialForm
def factorial(request):
    if (request.method == 'POST'):
        print(request.POST)
        return render(request, 'factorial.html')
    form_instance = FactorialForm()
    return render(request, 'factorial.html', {'form': form_instance})

from app1.forms import BmiForm
def bmi(request):
    if (request.method == 'POST'):
        print(request.POST)
        return render(request, 'bmi.html')
    form_instance = BmiForm()
    return render(request, 'bmi.html', {'form': form_instance})

from app1.forms import SignupForm
def signup(request):
    if(request.method=='POST'):
        print(request.POST)
        return render(request,'signup.html')
    form_instance=SignupForm()
    return render(request,'signup.html',{'form':form_instance})

from app1.forms import CalculatorForm
def calculator(request):
    if(request.method=='POST'):
        print(request.POST)
        form_instance=CalculatorForm(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            weight=int(data['weight'])
            height=int(data['height'])
            age=int(data['age'])
            gender=data['gender']
            ActivityLevel=data['ActivityLevel']
            print(weight,height,age,gender,ActivityLevel)
            if(gender=='Male'):
                bmr=10*weight+6.25*height-5*age+5
            else:
                bmr=10*weight+6.25*height-5*age-161
            calorie=bmr*float(ActivityLevel)
            print(calorie)
        return render(request,'calculator.html',{'result':calorie})
    if(request.method=='GET'):
        form_instance=CalculatorForm()
    return render(request,'calculator.html',{'form':form_instance})

from app1.forms import AddbookForm
def addbook(request):
    if(request.method=='POST'):
        print(request.POST)
        return render(request,'addbook.html')
    if(request.method=='GET'):
        form_instance=AddbookForm()
    return render(request,'addbook.html',{'form':form_instance})