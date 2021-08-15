from django.contrib import admin

from .models import Horario, Materia


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
