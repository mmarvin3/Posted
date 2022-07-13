from django.shortcuts import render
from .models import Poster
from django.views.generic.edit import CreateView, UpdateView, DeleteView



# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def posters_index(request):
    posters = Poster.objects.all()
    return render(request, 'posters/index.html', { 'posters': posters })

def posters_detail(request, poster_id):
    poster = Poster.objects.get(id=poster_id)
    return render(request, 'posters/detail.html', { 'posters': poster })

class PosterCreate(CreateView):
    model = Poster
    fields = ['name', 'type', 'description']
    success_url = '/posters/'

class PosterUpdate(UpdateView):
    model = Poster
    fields = ['name', 'type', 'description']

class PosterDelete(DeleteView):
    model = Poster
    success_url = '/posters/'
