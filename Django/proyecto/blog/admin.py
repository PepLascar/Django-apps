from django.contrib import admin
from .models import Category, Article

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)  #la coma está puesta así para que lo interprete como una tupla 

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'created_at', 'update_at')

    def save_model(self, request, obj, form, change): #comportamiento cuando se guarda un articulo en el modelo
        if not obj.user_id: # Si no me llega un user
            obj.user_id = request.user.id  #Si no está esta propiedad se le asigna un valor y guarda el objeto
        obj.save()

# Register your models here.
admin.site.register(Category, CategoryAdmin)   # Cargando el modelo Category para que funcione en el Admin
admin.site.register(Article, ArticleAdmin)     # Cargando modelo Article, tambipen le paso la clase con las fechas de cración