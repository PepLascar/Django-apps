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
# URL - VIEW - TEMPLATE
from django.contrib import admin
from django.urls import path
from django.conf import settings #accediendo a settings

from miapp import views # dos formas: 'from miapp import views' o 'import miapp.views'

urlpatterns = [ # Nombre del path | importe def del view |  name/id
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('inicio/', views.index, name="inicio"),
    path('holamundo-django/', views.holaMundo, name="hola_mundo" ),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('contacto/<str:nombre>/<str:apellido>', views.contacto, name="contacto"), #en la URL se pueden pasar parámetros en este caso /<str:nombre>
    path('pruebas/', views.pruebas, name="pruebas"),
    path('pruebas/<int:redirigir>/', views.pruebas, name="pruebas"),
    path('pagina/', views.pagina, name="pagina"),    
    path('donaciones/', views.donaciones, name="donaciones"),
    path('donaciones/<str:nombre>/', views.donaciones, name="donaciones"),
    path('donaciones/<str:nombre>/<str:apellido>/', views.donaciones, name="donaciones"),
    path('crear-articulo/<str:tittle>/<str:content>/<str:public>/', views.crear_articulo, name="crear-articulo"), #creando obj artículo por parámetro url
    path('articulo/', views.getArticulo, name="articulo"),
    path('editar-articulo/<int:id>', views.editarArticulo),
    path('articulos/', views.articulos, name="articulos"),
    path('borrar-articulo/<int:id>', views.borrar_articulo, name="borrar"),
    path('save-article/', views.save_article, name="save"),
    path('create-article/', views.create_article, name="create"),
    path('create-full-article/', views.create_full_article, name ="create_full")
]


# Configuración para cargar imágenes o carpetas  debug cuando se está el local, false cuando está en producción
if settings.DEBUG == True:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)