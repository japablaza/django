from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'gen/home.html')

def about(request):
    return render(request, 'gen/about.html', {'Extra':'Data'})

def page1(request):
    return HttpResponse('Simpe page')

def passwd(request):
    return HttpResponse('CLAVE')