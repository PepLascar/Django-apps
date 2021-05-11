from django.contrib import admin
from .models import Article, Categoria  #son los elementos que están en el modelo de la bd

class ArticleAdmin(admin.ModelAdmin): #es la clase que nos permite manupular los objetos desde el panel
    readonly_fields = ('crated_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)  #muestro en el modelo la fecha d creación de los objetos
admin.site.register(Categoria)

#Configuración título panel django/admin ... ya estáimportando el módulo admin 
titulo = "Proyecto 1 en Django"
admin.site.site_header = titulo
admin.site.site_title = "Administrador django 8"
#subtítulo
admin.site.index_title = "Administrador del proyecto 8"

