from enum import unique
from django.db import models
from ckeditor.fields import RichTextField  #importando la Def RichTextField del paquete de ck-editor (incorporar en app para ahcer bien el importe)

#Estos elementos son los que aparecen en mi Django admin
class Page(models.Model):  #heredando de los modelos de django
    title      = models.CharField(max_length=50, verbose_name='Título')
    content    = RichTextField(verbose_name='Contenido')  #configurando el TEXTFIELD CON CK-EDITOR
    slug       = models.CharField(unique=True, max_length=150, verbose_name="URL amigable") #esto nos permite definir una url (Unique = True . que ese campo sea único)
    order      = models.IntegerField(default=0,verbose_name="Orden") #ordenar los elementos en la nav-bar
    visible    = models.BooleanField(verbose_name="¿Visible?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")  #para guardar fecha del momento en que agregó un artículo
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

    class Meta: #Para modificar elementos de la página 
        verbose_name = "Página"
        verbose_name_plural = "Páginas"

    #Método para mostrar objetos de tipo Páge, imprimaun string. Con esto podré imprimir el título de cada página en el panel de administración
    def __str__(self):
        return self.title


"""
Para actualizar la base
- Hago el cambio
- makemigrations
- Agregarla a la basa pasarla a sql
- sqlmigrate + nombreapp + nummigración
- Se ha generado el sql.
- Ahora ejecutar el SQL para que se generen esos cambios
- python manage.py migrate
"""
