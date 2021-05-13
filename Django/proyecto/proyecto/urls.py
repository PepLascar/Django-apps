from django.contrib import admin
from django.urls import path

from mainapp import views #primero: importar views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="idx"),
    path('inicio/', views.index, name="index"),
    path('nosotros/', views.about, name="nosotros")
]
