from django.db import models

# Todos los modelos deberían estar dentro de una app.
# Tiene la definición de los campos que va a tener un objeto.
# Los modelos van definiendo las tablas que se va a tener en la BD
# https://docs.djangoproject.com/en/3.0/ref/models/fields/
#Las migraciones se ejecutan para que se vaya actualizando el modelo de la BD en las diferentes versiones del proyecto.

class Article(models.Model):  #está heredando de <-- representan a tablas en la base de datos
    tittle     = models.CharField(max_length=110, verbose_name = "Título")
    content    = models.TextField()
    image      = models.ImageField(default='null', verbose_name="Miniatura", upload_to="articles") #darle un path donde se van a cargar las imágenes (articles dentro del directorio media)
    public     = models.BooleanField(verbose_name = "¿Publicado?")
    crated_at  = models.DateTimeField(auto_now_add=True, verbose_name = "Creado") # guarda registro automáticamente con le fecha de adición
    updated_at = models.DateTimeField(auto_now=True, verbose_name = "Editado") # guarda la fecha de edición

    class Meta: #poner nombre sigular,plural,etc. Estas opciones sólo afectan el panel de administración
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
        ordering = ['-id'] #public, created_at

    def __str__(self):  #método mágico para transformar 
        if not self.public == True:   #if not muestra los privados, if los públicos
           public = "(publicado)"
        else:
            public = "(privado)"
        return f"{self.tittle} estado publicación: {public}"  #{self.crated_at }
       
       
class Categoria(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
    created_at = models.DateField()

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
