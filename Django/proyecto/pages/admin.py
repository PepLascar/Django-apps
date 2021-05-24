#CONFIGURACIONES PARA EL PANEL DE ADMINISTRACIÓN DE DJANGO - PAGES

from django.contrib import admin
from .models import Page

# CONFIGURACIONES EXTRA PARA EL MODELO
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    search_fields = ('title', 'content') #buscador por title y contenido
    list_filter = ('visible',) #mostrar solo los con campo visible, dejé la coma para que la reconozca como tupla
    list_display = ('title','visible','created_at')  #mostrar mas campos en la columna principal
    ordering = ('-created_at',)  #ordenar por ... recordar la , cuando son tuplas

# Registrar el modelo para que esté disponible en el oanel de administración
admin.site.register(Page, PageAdmin)

#CONFIGURACIÓN DEL PANEL
title = 'Proyecto 2 con Django'
subtitle = 'Panel de gestión'

admin.site.site_header = title
admin.site.site_title  = title  #título que aparece en la ventana del navegador
admin.site.index_title = subtitle

