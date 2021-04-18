#Hay diferentes tipos de shortcuts

from django.shortcuts import render, HttpResponse, redirect

# MVC vs MVT  -  En Django en controlador es la Vista que contiene -> Acciones

#Puedo hacer que este layout esté presente en todas las vistas del sitio concadenandolo en el return de los request http response
layout = """ 
<h1>Sitio web con Django | Jose Lascar </h1>
<hr/>
<ul>
    <li>
    <a href="/inicio">Inicio</a>
    </li>

    <li>
    <a href="/holamundo">Hola mundo</a>
    </li>

    <li>
    <a href="/nosotros">Nosotros</a>
    </li>

    <li>
    <a href="/contacto">Contacto</a>
    </li>

    <li>
    <a href="/donaciones">Donaciones</a>
    </li>

    <li>
    <a href="/pruebas">Pruebas</a>
    </li>    
</ul>
<hr/>
"""
# estos href están relacionados con el meny y su redirección


#AQUÍ prácticamente estoy reando PÁGINAS
def index(request):  #Método para crear el index
    html = """ 
            <h1>Inicio</h1>
            <p>Años hasta el 2050:</p>
            <ul>
    """
    year = 2021
    while year <= 2050:

        if year %2 == 0:
            html += f"<li>{str(year)}</li>"

        year += 1
    html += "</ul>"  #esto es para concadenar a var html el </ul>

    return HttpResponse(layout+html)

def nosotros(request):
    return HttpResponse(layout+"""
    <h1>Pagina para la web (Nosotros, servicios, donaciones, etc)</h1>
    <h2>Desarrollado por JLascar</h2>
    
    """)

def holaMundo(request):  #request parametro que permite recibir parametros para realizar las peticiones
    return HttpResponse(layout+"""   <h1> ONG - AYUDA A UN CANINO </h1>

    <div >   
        Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. 
        Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor 
        (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal 
        manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó 
        como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado
        en los 60s con la creación de las hojas "Letraset", las cuales contenian pasajes de Lorem Ipsum, y más 
        recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum.
    </div>

    <div>
        <h2>Nuestros integrantes</h2>
        <li>  Persona 1 - Cargo 1</li>
        <li>  Persona 2 - Cargo 2</li> 
        <li>  Persona 3 - Cargo 3</li>   
        <li>  Persona 4 - Cargo 4</li>  
    </div>

    <div>      <h2> Nuestros animales en ayuda:</h2>
        <h3>
        <p>Gato</p>
        <p>Perro</p>
        
        </h3>     </div>""")

def contacto(request, nombre, apellido): #def con parámetro vinculada con /<str:nombre>   El parámetro me lo devuelve en la página
    return HttpResponse(layout+
    f"<h1>Contacto {nombre}{apellido}</h1>")

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
        return redirect('contacto', nombre="Jose", apellido="Lascar") 
    return HttpResponse(layout+"""
    <h1>PRUEBAS</h1>
    <h2>PROBANDO ... ...</h2>
    
    """)
