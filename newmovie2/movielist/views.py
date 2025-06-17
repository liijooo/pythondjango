from django.shortcuts import render,redirect
from django.urls import reverse_lazy

def home(request):
    return render(request,'home.html')

# from movielist.forms import MovieForm
# def addmovie(request):
#     if (request.method=='POST'):
#         form_instance=MovieForm(request.POST,request.FILES)
#         if form_instance.is_valid():
#             form_instance.save()
#             return redirect('movielist:movielist')
#     form_instance=MovieForm()
#     return render(request, 'addmovie.html', {'form': form_instance})

from movielist.models import movie
from movielist.forms import MovieForm
from django.views.generic import CreateView, UpdateView, DeleteView


class AddMovie(CreateView):
    form_class=MovieForm
    template_name='addmovie.html'
    model=movie
    success_url=reverse_lazy('movielist:movielist')

from movielist.models import movie
from django.views.generic import ListView
class Movielist(ListView):
    model=movie
    template_name='movielist.html'
    context_object_name ='movies'


# def moviedetail(request,i):
#     m=movie.objects.get(id=i)
#     return render(request,'detail.html',{'movies':m})
from django.views.generic import DetailView
class MovieDetail(DetailView):
    model=movie
    template_name='detail.html'
    context_object_name='movies'


# def deletemovie(request,i):
#     m=movie.objects.get(id=i)
#     m.delete()
#     return redirect('movielist:movielist'

class DeleteMovie(DeleteView):
    model=movie
    template_name='deletemovie.html'
    success_url =reverse_lazy('movielist:movielist')

# def editmovie(request,i):
#     m=movie.objects.get(id=i)
#     if (request.method=='POST'):
#         form_instance=MovieForm(request.POST,request.FILES)
#         if form_instance.is_valid():
#             form_instance.save()
#             return redirect('movielist:movielist')
#     form_instance = MovieForm(instance=m)
#     return render(request, 'addmovie.html', {'form': form_instance})

from django.views.generic import UpdateView
class EditMovie(UpdateView):
    form_class = MovieForm
    template_name = 'editmovie.html'
    model=movie
    success_url = reverse_lazy('movielist:movielist')