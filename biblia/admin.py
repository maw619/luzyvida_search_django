from django.contrib import admin
from .models import Capitulo, Diccionario, Libro, Tema, Versiculo

@admin.register(Capitulo)
class CapituloAdmin(admin.ModelAdmin):
    list_display = ['numero', 'libro']
    search_fields = ['numero']

@admin.register(Diccionario)
class DiccionarioAdmin(admin.ModelAdmin):
    list_display = ['palabra', 'definicion']

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ['name', 'link1', 'link2']

@admin.register(Tema)
class TemaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'verso_start', 'verso_end']

@admin.register(Versiculo)
class VersiculoAdmin(admin.ModelAdmin):
    list_display = ['numero', 'contenido', 'capitulo']
    search_fields = ['contenido']
