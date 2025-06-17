from django.shortcuts import render,redirect

def home(request):
    return render(request,'home.html')

from movielist.forms import MovieForm
def addmovie(request):
    if (request.method=='POST'):
        form_instance=MovieForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('movielist:movielist')
    form_instance=MovieForm()
    return render(request, 'addmovie.html', {'form': form_instance})

from movielist.models import movie
def movielist(request):
    m=movie.objects.all()
    return render(request,'movielist.html',{'movies':m})


def moviedetail(request,i):
    m=movie.objects.get(id=i)
    return render(request,'detail.html',{'movies':m})


def deletemovie(request,i):
    m=movie.objects.get(id=i)
    m.delete()
    return redirect('movielist:movielist')

def editmovie(request,i):
    m=movie.objects.get(id=i)
    if (request.method=='POST'):
        form_instance=MovieForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('movielist:movielist')
    form_instance = MovieForm(instance=m)
    return render(request, 'addmovie.html', {'form': form_instance})
