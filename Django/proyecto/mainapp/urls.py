#URLS vinculadas a mainapp
from django.urls import path
from . import views #fichero dentro de la misma carpeta, el punto es para importar dede la carpeta actual

#recordar que tenemos templates con url amigables en el django admin
urlpatterns = [
    path('', views.index, name="idx"),
    path('inicio/', views.index, name="index"),
    path('registro/', views.register_page, name="registro"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout")
]
