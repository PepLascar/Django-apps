from django.http import request
from django.shortcuts import render, redirect  #redirect y renderizar
from django.contrib import messages  #mensajes flash que duran la actualización de 1 pantalla
from django.contrib.auth.forms import UserCreationForm  #autenticación usuario
from mainapp.forms import RegisterForm  #formulario de registro
from django.contrib.auth import authenticate, login, logout #módulo de autenticación


# Create your views here.

def index(request):
    return render(request, 'main/index.html', {
        'title': 'Inicio'
    })

def about(request):
    return render(request, 'main/about.html', {
        'title': 'Sobre nosotros'
    })

# view para el login de la página
def register_page(req):

    if req.user.is_authenticated:   #esto es para que si el usuario está ya autenticado no muestre el formulario de registro
        return redirect('/inicio')
    else:
            
        #register_form = UserCreationForm()
        register_form = RegisterForm()

        if req.method == 'POST':   # comprobar si el formulario ha sido enviado realmente 
            #register_form = UserCreationForm(req.POST) #pasarle los datos del formulario enviada por el parámetro
            register_form = RegisterForm(req.POST)

            if register_form.is_valid(): # Si es valido ...
                register_form.save()     # lo guardamos
                messages.success(req, 'Te has registrado correctamente!')  #mensaje flash
                return redirect('/inicio')         # y me redirecciona a             

        return render(req, 'users/register.html', {
            
            'title': 'Sistema de login', #contxto para pasarte un title
            'register_form': register_form
        })


def login_page(req):

    if req.user.is_authenticated:   #esto es para que si el usuario está ya autenticado no muestre el formulario de registro
        return redirect('/inicio')

    else:
        if req.method == 'POST':  #significa que está llegando información al formulario
            username = req.POST.get('username')
            password = req.POST.get('password')

            user = authenticate(req, username=username, password=password)

            if user is not None:  #si no es null ...
                login(req, user) #paso la req y el usuario que quiero identifiar
                return redirect('/inicio')
            else:
                messages.warning(req, 'No te has identificado correctamente')

        return render (req, 'users/login.html', {
            'title': 'Identificate'
        })


def logout_user(req):
    logout(req)
    return redirect ('login')



"""
- Crear view del login
- Crear template del login
- Vincular url del login
- Agregar opción del login al layout principal
- Importar módulo de autenticación de django
- Crear var con el formulario del módulo
- Llevar el register_form a la template_register
- En register.html crear el metodo post y el csrf token
- Heredar la view del formulario en la template
- validar y guardar el usuario -> redirigir a una página
- Crear un archivo en mainapp para manipular y personalizar el formulario
- Una vez hechas las configuraciones de que datos quiero del for en forms.py debo cargarlo en las vistas
- Importalo 

    - Crear función que contiene la lógica del login
    - Crear template que contendrá el login
    - Crear la url conectada con template de login
    - Luego en layout añadir el nuevo acceso al login para que el usuario lo vea
Para hacer funcionar el LOGIN 294.
    - importar módulo de autenticación
    - en def_login:
Para el LOGOUT 296.
    - Crear la vista del logout en views
    - usar método logout importado y darle la request
    - Cargarlo en la lay out dentro del if el usuario está loguedo
Para que los elementos no sean visibles desde cualquier parte a pesar de estar con logout 296
    - importar modulo de decorador en las otras apps (pages)

- import mensaje flash
- crear mensaje flash en la view, en el regiser valid
- heredar el mensaje en la template del index o en la que se requiera
"""