from django.contrib import admin
from .models import Page
# Registrar el modelo para que esté disponible en el oanel de administración

admin.site.register(Page)

#CONFIGURACIÓN DEL PANEL
title = 'Proyecto 2 con Django'
subtitle = 'Panel de gestión'

admin.site.site_header = title
admin.site.site_title  = title  #título que aparece en la ventana del navegador
admin.site.index_title = subtitle

