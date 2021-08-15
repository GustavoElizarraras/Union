
from django.contrib import admin
from aportes.models import Aporte , Tag
# Register your models here.

@admin.register(Aporte)

class AporteAdmin(admin.ModelAdmin):
    list_display = ('pk','alumno','titulo','descripcion','link')
    list_display_links = ('pk','titulo')

    search_fields= (
        'alumno',
        'titulo',
        'link',
        'tags',
        )

@admin.register(Tag)

class AporteAdmin(admin.ModelAdmin):
    list_display = ('nombreTag',)
    list_display_links = ('nombreTag',)
    search_fields= (
        'nombreTag',
        )
