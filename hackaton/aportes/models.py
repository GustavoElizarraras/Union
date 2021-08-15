from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):
    nombreTag  = models.CharField('Tag', max_length=200)

    def __str__(self) :
        return self.nombreTag

class Aporte(models.Model):
    alumno = models.ForeignKey(User, on_delete=CASCADE)
    tags = models.ManyToManyField(Tag, blank=True, related_name='tag')
    titulo = models.CharField('Titulo', max_length=200)
    link = models.URLField('Link', max_length=400)
    descripcion = models.CharField('Descripcion', max_length= 2000)

    def __str__(self) :
        return 'Titulo: {} | Alumno: {} | Tags:{} | link:{} '.format(self.titulo, self.alumno, self.tags,self.link)

