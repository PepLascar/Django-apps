#URLS vinculadas a BLOG
from django.urls import path
from . import views #fichero dentro de la misma carpeta

#recordar que tenemos templates con url amigables en el django admin
urlpatterns = [
    path('articulos/', views.list, name="list"),
    path('categoria/<int:category_id>', views.category, name="category"),
    path('articulo/<int:article_id>', views.article, name="article")
]
