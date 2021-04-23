"""firstDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#Aquí se agregan las url para usarlas desde las views con el html
from django.contrib import admin
from django.urls import path

#importar app con las vistas que quiero trabajar
#puedo importar de dos formas: 'from miapp import views' o 'import miapp.views'

#from miapp import views
import miapp.views

#el primer parametro es el nombre del path que se utiliza para visitar la url  -  Primer parámetro es el URL
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', miapp.views.index, name="index"),
    path('inicio/', miapp.views.index, name="inicio"),
    path('holamundo-django/', miapp.views.holaMundo, name="hola_mundo" ),
    path('nosotros/', miapp.views.nosotros, name="nosotros"),
    path('contacto/<str:nombre>/<str:apellido>', miapp.views.contacto, name="contacto"), #en la URL se pueden pasar parámetros en este caso /<str:nombre>

    path('pruebas/', miapp.views.pruebas, name="pruebas"), #parámetros-opcionaes
    path('pruebas/<int:redirigir>/', miapp.views.pruebas, name="pruebas"),

    path('pagina/', miapp.views.pagina, name="pagina"),    

    path('donaciones/', miapp.views.donaciones, name="donaciones"), #parámetros-opcionaes
    path('donaciones/<str:nombre>/', miapp.views.donaciones, name="donaciones"),
    path('donaciones/<str:nombre>/<str:apellido>/', miapp.views.donaciones, name="donaciones")
]
