from enum import unique
from django.db import models

class Page(models.Model):  #heredando de los modelos de django
    title      = models.CharField(max_length=50, verbose_name='Título')
    content    = models.TextField(verbose_name='Contenido')
    slug       = models.CharField(unique=True, max_length=150, verbose_name="URL amigable") #esto nos permite definir una url (Unique = True . que ese campo sea único)
    visible    = models.BooleanField(verbose_name="¿Visible?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")  #para guardar fecha del momento en que agregó un artículo
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

    class Meta: #Para modificar elementos de la página 
        verbose_name = "Página"
        verbose_name_plural = "Páginas"

    #Método para mostrar objetos de tipo Páge, imprimaun string. Con esto podré imprimir el título de cada página en el panel de administración
    def __str__(self):
        return self.title
