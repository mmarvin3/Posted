from unicodedata import name
from django.db import models

# Create your models here.
class Poster():
    def __init__(self, name, type, description):
        self.name = name
        self.type = type
        self.description = description

posters = [
    Poster('Rush Hour', 'movie', 'A poster of Jackie Chan and Chris Tucker starring in the Rush Hour movie'),
    Poster('Succession', 'tv show', 'A poster of the all the characters in the show Succession'),
    Poster('Harry Potter', 'book', 'A poster of the book cover of the first Harry Potter book')
]