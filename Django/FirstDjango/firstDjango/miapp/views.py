from django.shortcuts import render, HttpResponse, redirect #Hay diferentes tipos de shortcuts
from miapp.models import Article
from django.db.models import Q #funcionalidad or
from miapp.forms import FormArticle  #importando esa clase para poder utilizanla
from miapp import views # ??
from django.contrib import messages  #Mensajes flash: desaparecen con una actualización

layout = ""

#AQUÍ prácticamente estoy creando PÁGINAS
def index(request):  #Método para crear el index
    """
    html = ""
    <h1>Inicio</h1>
    <p>Años hasta el 2050</p>
    <ul>
    ""
    year = 2021
    while year <= 2050:

        if year %2 == 0:
            html += f"<li>{str(year)}</li>"
        year += 1
    html += "</ul>"  #esto es para concadenar a var html el </ul>
    """

    year = 2021
    hasta = range(year, 2051)

    nombre = None
    #Trabajando con lista
    lenguajes = ['Boostrap','JavaScript','Django','Vue']
    
    #Aquí paso los datos de la vista a la plantilla html
    return render(request,'index.html',{
        'title' : 'Inicio',
        'mi_variable' : 'Soy un dato que está en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': hasta
    })

def nosotros(request):
    return render(request, 'nosotros.html') 

def holaMundo(request):  #request parametro que permite recibir parametros para realizar las peticiones
    return render(request, 'hola_mundo.html') #llamado desde templates

def contacto(request, nombre, apellido): #def con parámetro vinculada con /<str:nombre> Para que funcione esta def tengo que darle 2 parámetros en la url
    return HttpResponse(layout+
    f"<h1>Contacto {nombre} {apellido}</h1>")

def donaciones(request, nombre="", apellido=""):  #PARÁMETROS OPCIONALES - aguanta 1-2-3 parámetros
    if nombre or apellido:
        html = f"<h3>Usuario: {nombre} {apellido}</h3>"
        gracias = f"<h1> Gracias por donar {nombre} {apellido}</h1>"
    else:
        html = ""
        gracias=""
    return HttpResponse(layout+html+gracias)

def pruebas(request, redirigir=0):  #REDIRECCIÓN en este caso a /inicio/

    if redirigir == 1:
        return redirect('pagina') 
    return HttpResponse(layout+"""
    <h1>Ingresar número para redirigir: </h1>
    """)

def pagina(request):
    return render(request, 'pagina.html', {
        'texto': '',
        'lista': ['uno', 'dos', 'tres']
    })

def crear_articulo(request, tittle, content, public):  #CREAR UN OBJETO ARTICULO DENTRO DE LA BD - atributos del objeto articulo. Variable con parámetro que entrega el valor
    articulo = Article(
        tittle = tittle,
        content = content,
        public = public       
    )
    articulo.save() #para guardar un artículo obj en la bd  
    return HttpResponse(f"Artículo  {articulo.tittle} - {articulo.content } ")


def save_article(request):  #CREAR artículo sin parámetro por URL, todo por FORMULARIO, deben haber variables que reciban los datos.
    if request.method == 'POST':
        
        tittle = request.POST['title']  #Validación
        if len(tittle) < 4:
            return HttpResponse("Título muy pequeño")

        content = request.POST['content']
        public  = request.POST['public']

        articulo = Article(
            tittle = tittle,
            content = content,
            public = public       
        )

        articulo.save()
        print("Consola 110")
        #return HttpResponse(f"Artículo creado {articulo.tittle} - {articulo.content } - {request.method} ")
        return redirect('articulos')

    else:
        return HttpResponse("<h2> No se ha podido crear el artículo </h2>")


def create_article(request):
    return render(request, 'create-article.html')


def create_full_article(request): 

    if request.method == 'POST':
        print("Consola 124")
        formulario = FormArticle(request.POST)  

        if formulario.is_valid():    #is_valid evalúa las condiciones de validación que se configuran
            print("Consola 139")
            data_form = formulario.cleaned_data #datos limpios que llegan del formulario

            tittle   = data_form.get('title')
            content = data_form.get('content')
            public  = data_form['public']
                                            #Variables para recoger la información del cleaned data
            articulo = Article(
                tittle = tittle,
                content = content,
                public = public
            )

            articulo.save()
            # Crear mensaje flash que solo de muestra 1 vez(actualización)
            messages.success(request, f'Has creado exitosamente un artículo {articulo.id}' )
            return redirect('articulos')

            #return HttpResponse(articulo.title + ' - ' + articulo.content+' - ' + str(articulo.public))
    else:
        formulario = FormArticle()
        print("Consola 145")
    return render(request, 'create_full_article.html', {
        'form': formulario       
    })

def getArticulo(req): #Se puede entregar parámetro fijo o por url
    try:
        #articulo = Article.objects.get(pk=9)
        articulo = Article.objects.get(tittle="hooa", public=True) #Lo encuentra y lo muestra
        response = f"Articulo:  <br/> {articulo.id} - {articulo.tittle}"
    except: 
        response = "<h1>Artículo no encontrado</h1>"

    return HttpResponse(response)  #retornando la respuesta del try catch

def editarArticulo(req, id): #EDITAR ARTÍCULOS
    articulo = Article.objects.get(pk=id) #voy a buscar por la pk/id id artículo

    articulo.tittle  = "Electrónica"
    articulo.content = "Productos"
    articulo.public  = True

    articulo.save() # Guardo cambios. Editando objeto ya existente identificado por su id

    return HttpResponse(f"Artículo {articulo.id} editado {articulo.tittle} - {articulo.content } ")
 
def articulos(request): #LISTAR ARTÍCULOS

    #articulos = Article.objects.all().order_by('-id') #Obtener todos los elementos de la base de datos.
    #articulos = Article.objects.order_by('id')  #  '-id',  '-tittle',  [3:7]limit
    articulos = Article.objects.filter(public=True).order_by('-id')  #Filter permite por tittle__contains="" id =, tittle__contains, tittle__exact, _iexact, id__gt=12, lt=10
    """articulos = Article.objects.filter(tittle__contains="Articulo",
                                        #public=
    ).exclude(
        public=False  #puedo cambiar el estado de quien quiero excluir
    )"""
    
    """
    articulos = Article.objects.filter(
        Q(tittle__contains="2") | Q(public=True)  #OR
    )"""

    #articulos = Article.objects.raw("SELECT * from miapp_article WHERE tittle='articulo 2' and public=0 ")

    return render(request, 'articulos.html',{
        'articulos': articulos
    })

def borrar_articulo(req, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')





