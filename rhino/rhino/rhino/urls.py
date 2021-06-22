"""rhino URL Configuration

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
from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('index/', views.index, name="inicio"),
    path('registro/', views.registro, name="registro"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.desconectarse, name="desc"),
    path('holamundo/', views.holamundo, name="holamundo"),
    path('donar/', views.donar, name="donar"),
    path('listar/', views.listar, name="listar"),
    path('crear/', views.crear, name="crear"),
    path('editar/<pk>', views.editar, name="editar"),
    path('eliminar/<pk>', views.eliminar, name="eliminar")
]

#para las imágenes
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
