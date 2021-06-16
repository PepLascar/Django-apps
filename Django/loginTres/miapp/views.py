from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm #Lo dejé de usar para personalizar register form.
from django.contrib.auth import authenticate, login, logout
from miapp.forms import RegisterForm, FormArticle #RegisterForm de forms.py
from django.contrib.auth.decorators import login_required #Decoradores
from miapp.models import Category, Article
from django.contrib.auth.models import User

# https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html

@login_required(login_url="login") #Decorador, lista, articulos, etc
def index(req):
    return render (req, 'index.html', {
        'title': 'Inicio'
    })

@login_required(login_url="login") #Decorador
def holamundo(req):
    return render(req, 'holamundo.html', {
        'title': 'Hola Mundo!'
    })

def donar(req):
    return render(req, 'donar.html',{
        'title': 'Donaciones'
    })

def registro(req):    
    if req.user.is_authenticated:   #esto es para que si el usuario está ya autenticado no muestre el formulario de registro
        return redirect('/index')

    else:        
        register_form = RegisterForm() # /register_form = UserCreationForm()

        if req.method == 'POST':   # comprobar si el formulario ha sido enviado realmente 
            #register_form = UserCreationForm(req.POST) #pasarle los datos del formulario enviada por el parámetro
            register_form = RegisterForm(req.POST)

            if register_form.is_valid(): # Si es valido...
                register_form.save()     # objeto register form guardado...
                messages.success(req,'Ahora te puedes loguear. ¡Te has registrado correctamente!')  #mensaje flash

                return redirect('/index')          
        
        return render(req, 'registro.html', {            
            'title': 'Registro de usuario', #contxto para pasarte un title y usarlo desde lay out.
            'register_form': register_form
        })

def login_page(req):
    if req.user.is_authenticated:   #Si el usuario está ya autenticado no muestre el formulario de registro.
        return redirect('/index')

    else:

        if req.method == 'POST':  #significa que está llegando información al formulario
            print('consola 45')
            username = req.POST.get('username')
            password = req.POST.get('password')

            user = authenticate(req, username=username, password=password)

            if user is not None:  #Si no es null ...                   
                print('Consola 51')                
                login(req, user) #paso la req y el usuario que quiero identifiar
                return redirect('/index')

            else:
                messages.warning(req, 'No te has identificado correctamente =(')

        return render (req, 'login.html', {
            'title': 'Login'
        })

def desconectarse(req):
    logout(req)
    return redirect ('login')


# --- Listar Artículos con Categorías ---
@login_required(login_url='login')
def crear(request): 

    if request.method == 'POST':
        print("Consola 124")
        formulario = FormArticle(request.POST)  

        if formulario.is_valid():    #is_valid evalúa las condiciones de validación que se configuran
            print("Consola 139")
            data_form = formulario.cleaned_data #datos limpios que llegan del formulario
            
            user = getattr(request, 'user', None)
            title   = data_form.get('title')
            content = data_form.get('content')
            public  = data_form['public']
                            #Variables para recoger la información del cleaned data
            articulo = Article(
                user = user,
                title = title,
                content = content,
                public = public
            )
            print(f' Usuario: {user}')
            articulo.save()

            # Crear mensaje flash que solo de muestra 1 vez(actualización)
            messages.success(request, f'Has creado exitosamente un artículo {articulo.id}' )
            return redirect('index')

            #return HttpResponse(articulo.title + ' - ' + articulo.content+' - ' + str(articulo.public))
    else:
        formulario = FormArticle()
        print("Consola 145")
    return render(request, 'crear.html', {
        'form': formulario       
    })

#@login_required(login_url='login')
def listar(req):

    articles = Article.objects.all()  # Traer/obtener todos los objetos (articulos)

    return render(req, 'listar.html', {
        'title': 'Artículos',
        'articles': articles   #devolver esta variable
    })

def eliminar(req, pk):
    articulo = Article.objects.get(pk=pk) #instancia del articulo que quiero eliminar
    articulo.delete() # elimino esa objeto instanciado 
    return redirect('listar')

#    user = getattr(request, 'user', None)
#-----------------------------------------------------
def editar(req, pk):
    articulo = Article.objects.get(id=pk) # variable con objeto Article del modelo
    print(f'oo oo {id}')
    datos = {
        'form': FormArticle(Article.objects.get(instance=articulo))
    }
    print('141 141')
    if req.method == 'POST':
        print(' 8888 ')
        formulario_edit = FormArticle(data=req.POST, instance=articulo)  # conjunto de datos a grabar, mediante la instancia del objeto
        if formulario_edit.is_valid:
            formulario_edit.save()
            datos['mensaje'] = "Vehículo Editado Correctamente"
    return render(req, 'editar.html', datos)


def editar(req, pk):
    articulo = Article.objects.get(articuloid=pk) # variable con objeto Article del modelo
    print(f'oo oo {articulo}')
    datos = {
        'form': FormArticle(instance=articulo)
    }
    print('141 141')
    if req.method == 'POST':
        formulario_edit = FormArticle(data=req.POST, instance=articulo)  # conjunto de datos a grabar, mediante la instancia del objeto
        if formulario_edit.is_valid:
            formulario_edit.save()
            datos['mensaje'] = "Vehículo Editado Correctamente"
    return render(req, 'editar.html', datos)


#-----------------------------------------------------
def category(req, category_id):
    category = Category.objects.get(id=category_id)

    return render(req, 'categories/category.html', {
        'category': category
        #'articles': articles
    })
