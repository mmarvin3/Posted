from django.shortcuts import render
from .models import Poster


# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# class Poster():
#     def __init__(self, name, type, description):
#         self.name = name
#         self.type = type
#         self.description = description

# posters = [
#     Poster('Rush Hour', 'movie', 'A poster of Jackie Chan and Chris Tucker starring in the Rush Hour movie'),
#     Poster('Succession', 'tv show', 'A poster of the all the characters in the show Succession'),
#     Poster('Harry Potter', 'book', 'A poster of the book cover of the first Harry Potter book')
# ]

def posters_index(request):
    posters = Poster.objects.all()
    return render(request, 'posters/index.html', { 'posters': posters })

def posters_detail(request, poster_id):
    poster = Poster.objects.get(id=poster_id)
    return render(request, 'posters/detail.html', { 'posters': poster })
