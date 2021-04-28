from django.db import models

# Todos los modelos deberían estar dentro de una app.
# Tiene la definición de los campos que va a tener un objeto.
# Los modelos van definiendo las tablas que se va a tener en la BD
# https://docs.djangoproject.com/en/3.0/ref/models/fields/

#Las migraciones se ejecutan para que se vaya actualizando el modelo de la BD en las diferentes versiones del proyecto.

class Article(models.Model):  #está heredando de <-- representan a tablas en la base de datos
    tittle     = models.CharField(max_length=110)
    content    = models.TextField()
    image      = models.ImageField(default='null')
    public     = models.BooleanField()
    crated_at  = models.DateTimeField(auto_now_add=True) # guarda registro automáticamente con le fecha de adición
    updated_at = models.DateTimeField(auto_now=True) # guarda la fecha de edición

class Categoria(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
    created_at = models.DateField()
