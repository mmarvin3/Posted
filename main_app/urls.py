from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('posters/', views.posters_index, name='index'),
    path('posters/<int:poster_id>/', views.posters_detail, name='detail'),
]
