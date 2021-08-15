from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

from usuarios.models import Alumno

class Grupo(models.Model):
    nombre = models.CharField('Nombre del grupo', max_length=20)
    def __str__(self):
        return self.nombre

class Hora(models.Model):
    hora = models.CharField('Hora', max_length=50)
    def __str__(self):
        return self.hora

class Horario(models.Model):
    lunes = ForeignKey(Hora, on_delete=models.CASCADE)
    martes = ForeignKey(Hora, on_delete=models.CASCADE)
    miercoles = ForeignKey(Hora, on_delete=models.CASCADE)
    jueves = ForeignKey(Hora, on_delete=models.CASCADE)
    viernes = ForeignKey(Hora, on_delete=models.CASCADE)
    sabado = ForeignKey(Hora, on_delete=models.CASCADE)
    domingo = ForeignKey(Hora, on_delete=models.CASCADE)
    def __str__(self):
        return 'Lunes: {} \n Martes: {} \n Miercoles: {} \n Jueves: {} \n Viernes: {} \n Sabado: {} \n Domingo: {}'.format(self.lunes, self.martes, self.miercoles, self.jueves, self.viernes, self.sabado, self.domingo)

class nombre_Materia(models.Model):
    nombre = models.CharField('Nombre de la materia', max_length=100)
    def __str__(self):
        return self.nombre
class Licenciatura(models.Model):
    nombreLicenciatura = models.CharField('Nombre de la licenciatura', max_length=200)

class Materia(models.Model):
    nombreMateria = models.ForeignKey('nombre_Materia',on_delete=CASCADE)
    grupo = models.ForeignKey('Grupo', on_delete=CASCADE)
    horario =models.ForeignKey('Horario', on_delete=CASCADE)
    licenciatura = models.ForeignKey('Licenciatura', on_delete=CASCADE)
    def __str__(self):
        return 'Materia: {} \n Grupo: {} \n Licenciatura: {} \n'.format(self.nombreMateria, self.grupo, self.licenciatura)

class Escuela(models.Model):
    nombre = models.CharField('Nombre de la escuela', max_length=200)
    def __str__(self):
        return self.nombre

class GrupoEstudio(models.Model):
    nombreGrupoEstudio = models.ForeignKey('nombre_Materia', on_delete=CASCADE)
    escuela = models.ForeignKey('Escuela', on_delete=CASCADE)
    alumnos = models.ForeignKey(Alumno, on_delete=CASCADE)
