from django.contrib import admin
from usuarios.models import Alumno
# Register your models here.

@admin.register(Alumno)

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('pk','user','escuela','licenciatura')
    list_display_links = ('pk','user')

    search_fields= (
        'user__email',
        'user__first_name',
        'user__last_name',
        'escuela',
        'licenciatura',
        )
