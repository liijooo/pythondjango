from django.shortcuts import render

from movielist.forms import MoviesForm
def home(request):
    if(request.method=='POST'):
        print(request.POST)
        return render(request,'home.html')
    if(request.method=='GET'):
        form_instance=MoviesForm()
        return render(request,'home.html',{'form':form_instance})

def addmovie(request):
    form_instance = MoviesForm()
    return render(request, 'home.html', {'form': form_instance})


