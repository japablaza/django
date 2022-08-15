from django.db import models
from datetime import date, time
from django.utils import timezone

class oficinas(models.Model):
    nombre      = models.CharField(max_length=150)
    codigo      = models.CharField(max_length=10)
    numero      = models.IntegerField(default=1)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Codigo: {self.codigo} - Numero: {self.numero}"

class salas(models.Model):
    nombre_sala = models.CharField(max_length=150)
    codigo_de_la_sala   = models.CharField(default="Sala A", max_length=100)
    dia         = models.DateField(default=timezone.now())
    max_time    = models.IntegerField(default=1)
    inicio      = models.TimeField(default=time(8))
    oficina     = models.ForeignKey(oficinas, on_delete=models.CASCADE)    
    
    def __str__(self):
        return f"Reunion en la sala {self.nombre_sala}, el dia {self.dia}, a las {self.inicio}"
    