from django.shortcuts import render

from django.http import HttpResponse

# Define the home view
def home(request):
    return HttpResponse('Hello')

def about(request):
    return render(request, 'about.html')
