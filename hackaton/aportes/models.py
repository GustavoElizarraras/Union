from django.db import models
from django.db.models.deletion import CASCADE
from usuarios.models import Alumno
# Create your models here.

class Tag(models.Model):
    nombreTag  = models.CharField('Tag', max_length=200)

class Aporte(models.Model):
    tags = models.ManyToManyField(Tag,on_delate=CASCADE)
    titulo = models.CharField('Titulo', max_length=200)
    link = models.URLField('Link', max_length=400)
    descripcion = models.CharField('Descripcion', max_length= 2000)