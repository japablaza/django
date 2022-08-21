from django.http import HttpResponse
# from django.shortcuts import render
from datetime import datetime

# Create your views here.


def inicio(request):
    return HttpResponse("This is the main page, Bienvenidos!", {"message": "Hola Tulio!!!"})

def lahora(request):
    return(HttpResponse(f"La fecha y hora actual: {datetime.now()}"))