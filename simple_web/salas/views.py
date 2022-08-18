from django.shortcuts import render, get_list_or_404

from .models import salas
# Create your views here.

def more_info(request, id):
    sala = get_list_or_404(salas, pk=id) 
    return render(request, "salas/masinfo.html", {"reunion": sala})