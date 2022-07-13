from django.shortcuts import redirect, render
from .models import Poster
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def posters_index(request):
    posters = Poster.objects.filter(user=request.user)
    return render(request, 'posters/index.html', { 'posters': posters })

@login_required
def posters_detail(request, poster_id):
    poster = Poster.objects.get(id=poster_id)
    return render(request, 'posters/detail.html', { 'posters': poster })

class PosterCreate(CreateView):
    model = Poster
    fields = ['name', 'type', 'description']
    success_url = '/posters/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PosterUpdate(UpdateView):
    model = Poster
    fields = ['name', 'type', 'description']

class PosterDelete(DeleteView):
    model = Poster
    success_url = '/posters/'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)