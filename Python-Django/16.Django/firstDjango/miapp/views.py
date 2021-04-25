#Hay diferentes tipos de shortcuts
from django.shortcuts import render, HttpResponse, redirect

# MVC vs MVT  -  En Django en controlador es la Vista que contiene -> Acciones
# estos href están relacionados con el meny y su redirección

layout = ""

#AQUÍ prácticamente estoy reando PÁGINAS
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

def contacto(request, nombre, apellido): #def con parámetro vinculada con /<str:nombre>   El parámetro me lo devuelve en la página
    return HttpResponse(layout+
    f"<h1>Contacto {nombre} {apellido}</h1>")

def donaciones(request, nombre="", apellido=""):  #PARÁMETROS OPCIONALES

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

    def pag():
        return render(request, 'pa')