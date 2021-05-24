from django import forms   #formularios
from django.core import validators #validadores

from django.contrib.auth.forms import UserCreationForm #formularios por defecto
from django.contrib.auth.models import User  #importal el modelo de Usuario para crear el formulario

# formulario creado en base a una clase
class RegisterForm(UserCreationForm)  :
    class Meta:
        model  = User  #modelo en el cual se va a basar el formulario
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']    #campos que tiene el modelo que quiero representar visualmente en el formulario
        
