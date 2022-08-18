from django.shortcuts import render
from django.http import HttpResponse
import time

from salas.models import salas

num_salas = {'numero': salas.objects.count()}

def inicio (request):
    return render(request, "simple_web/welcome.html",
    num_salas)

def sobremi (request):
    return HttpResponse("This page is about me")

# def lahora(request):
#     return HttpResponse(f'This is the time in CR: '+ time.strftime('%a %s: %Z\n'))
def lahora (request):
    return render(request, "salas/salas.html", num_salas)