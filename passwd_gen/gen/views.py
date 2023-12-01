from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'gen/home.html', {'tag': 'palabra'})

def about(request):
    return HttpResponse('About the author')