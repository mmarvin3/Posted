from audioop import reverse
from unicodedata import name
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Poster(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'poster_id': self.id})
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Photo(models.Model):
    url = models.CharField(max_length=200)
    poster = models.ForeignKey(Poster, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for cat_id: {self.poster_id} @{self.url}"