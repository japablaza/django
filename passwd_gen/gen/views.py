from django.shortcuts import render
from django.http import HttpResponse
import random
import string

# Create your views here.

def home(request):
    return render(request, 'gen/home.html')

def about(request):
    return render(request, 'gen/about.html', {'Extra':'Data'})

def page1(request):
    return HttpResponse('Simpe page')

def passwd(request):

    clave = ''
    letras       = list(string.ascii_lowercase)
    alfabeto_up  = list(string.ascii_uppercase)
    especial     = list(set(string.punctuation))
    numeros      = list('0123456789')

    if request.GET.get('mayuscula'):
        letras.extend(alfabeto_up)
    if request.GET.get('especiales'):
        letras.extend(especial)
    if request.GET.get('numeros'):
        letras.extend(numeros)

    largo = int(request.GET.get('largo', 20))

    for letra in range(largo):
        clave += random.choice(letras)

    return render(request, 'gen/clave.html', {'passwd': clave})