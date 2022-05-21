from django import urls
from django.urls import path
from .views import registro, loguear, desconectarse

urlpatterns = [
    path('registro/', registro, name='registro' ),
    path('login/', loguear, name="login"),
    path('logout/', desconectarse, name="logout"),
]

