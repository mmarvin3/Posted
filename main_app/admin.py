from django.contrib import admin

from .models import Photo, Poster

admin.site.register(Poster)
admin.site.register(Photo)