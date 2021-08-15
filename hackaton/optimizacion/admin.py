from django.contrib import admin

from .models import Horario, Materia, Grupo, Hora, nombre_Materia, Licenciatura, Escuela, GrupoEstudio


@admin.register(Horario)

class HorarioAdmin(admin.ModelAdmin):
    list_display = ('lunes','martes','miercoles','jueves','viernes','sabado','domingo')
    list_display_links = ('lunes','martes','miercoles','jueves','viernes','sabado','domingo')



@admin.register(Materia)

class MateriaAdmin(admin.ModelAdmin):
    list_display = ('pk','nombreMateria','grupo','horario','licenciatura')
    list_display_links = ('pk','nombreMateria')

    search_fields= (
        'nombreMateria',
        'grupo',
        'horario',
        'licenciatura',
        )

@admin.register(Grupo)

class GrupoAdmin(admin.ModelAdmin):
    list_display = ('pk','nombre')

@admin.register(Hora)

class HoraAdmin(admin.ModelAdmin):
    list_display = ('pk','hora')

@admin.register(nombre_Materia)
class NombreMateriaAdmin(admin.ModelAdmin):
    list_display = ('pk','nombre')

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('pk','nombreLicenciatura')

@admin.register(Escuela)
class EscuelaAdmin(admin.ModelAdmin):
    list_display = ('pk','nombre')

@admin.register(GrupoEstudio)
class GrupoEstudioAdmin(admin.ModelAdmin):
    list_display = ('pk','nombreGrupoEstudio','escuela','alumnos')