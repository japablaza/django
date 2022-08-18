from django.shortcuts import render
from django.http import HttpResponse
import time

def inicio (request):
    return render(request, "simple_web/welcome.html")

def sobremi (request):
    return HttpResponse("This page is about me")

# def lahora(request):
#     return HttpResponse(f'This is the time in CR: '+ time.strftime('%a %s: %Z\n'))
def lahora (request):
    return render(request, "salas/salas.html")