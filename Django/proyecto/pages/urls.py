#URLS vinculadas a pages
from django.urls import path
from . import views #fichero dentro de la misma carpeta

#recordar que tenemos templates con url amigables en el django admin
urlpatterns = [
    path('pagina/<str:slug>', views.page, name="page"),
]
