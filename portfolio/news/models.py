from django.db import models

# Create your models here.
class Project(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.CharField(max_length=300)
    image = models.ImageField(upload_to='news/images/')

