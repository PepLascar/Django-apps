from django.db import models

class Category(models.Model): # usar funcionalidades del módulo models
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.CharField(max_length=255,verbose_name='Descripción')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Creado el')
    #Configuraciones para el panel de administración
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    #Método mágico, cuando yo imprima un objeto representará un objeto de la 'categoría' que haya en la BD
    def __str__(self):
        return self.name