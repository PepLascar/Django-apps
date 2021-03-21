import os
os.system("cls")

"""

FUNCIONES:
Conjunto de instrucciones agrupadas bajo un nombre concreto que puedes reutilizarse invocando a la función tantas veces como sea necesario.

def nombreFuncion (parametro1, parametro2):
    #Lógica / instrucciones de la función

nombreFuncion (parametro_a)
nombreFuncion (parametro_b)

"""

#Ejemplo 1

#Definir función
def mostrarNombre():
    print('Usando función mostrarNombre \n')

#Invocar función (llamar, ejecutar)
mostrarNombre()



#Ejemplo 2 - Parámetros

#nombre = input("Nombre usuario: ")

def nombreUsuario(nombre, edad):
    print(f"Nombre usuario: {nombre}")

    if edad >= 18:
        print("Ud. es mayor de edad")
    else:
        print("Ud. es menor de edad")
#----------------------------------------

nombre_usuario = input("Ingrese nombre usuario: ")
edad = int(input("Edad: "))

nombreUsuario(nombre_usuario, edad)

#Ejemplo 3
def tablaMultiplicar (tabla):
    
    #tabla = int(input('De que númmero quieres la tabla: '))
    if tabla < -1 :
        tabla = 1

    print(f'##La tabla de múltiplicar del número {tabla}##')

    for i in range (0,10):

        if tabla == 45 or tabla == 0:
            print('No se puede mostrar esa tabla')
            break

        print(f'{tabla} x {i} = {tabla*i}')
    else:
        print(f'Fin del ciclo (else)')
#-----------------------------------------------------------
tabla = int(input('De que númmero quieres la tabla: '))
tablaMultiplicar(tabla)

#Ejemplo 3.1   Aquí se muestran todas las tablas de multiplicar ya que la Fn usa la iteración de i
"""
for i in range (1,11):
    tablaMultiplicar(i)
"""

#Ejemplo 4 - Parámetros opcionales
def getEmpleado (nombre, rut = False):   #poniendole un boolean/none admite que un parámetro no sea ingresado
    print(f"-Empleado- \nNombre: {nombre} \nRut: {rut}")
    if rut == False:
        print("Falta completar rut usuario.")

getEmpleado("Jose")


#Ejemplo 5 - Return
def saludar(nombre):
    saludo = f"Hola {nombre}"
    return saludo
print(saludar("Jose"))


def calculadora(num1, num2, basicas = False): #Ese false es prácticamente una Flag
    suma  = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    div   = num1 / num2

    print("\n")
    cadena = ""

    if basicas != False:

        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " +str(resta)
        cadena += "\n"
    else:
        cadena += "Multi: " + str(multi)
        cadena += "\n"
        cadena += "Div: "   + str(div)

    return cadena

print(calculadora(5,5))

#Ejemplo 7
def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellido(apellido):
    texto = f"Apellido: {apellido}"
    return texto

def nombreCompleto(nombre, apellido):
    texto = getNombre(nombre) + "\n" + getApellido(apellido)
    return texto

print(nombreCompleto("Jose ","Lascar"))
#print(getNombre("Jose"),"\n",getApellido("Lascar"))


#Ejemplo 8 - Funciones Lambda (anónimas, simples, para tareas repetitivas) - Definida en 1 linea.
que_anio = lambda year: f"El año es {year}"
print(que_anio(2021))

#Ejemplo 9
"""
Variables locales: Se define dentro de la Fn y no se puede usar fuera de ella. Está solamente disponible dentro a no ser que se use un Return para sacarla.
Variables globales: Son las que se declaran fuera de una Fn y están disponibles dentro y fuera de la Def.
"""

def holaMundo():
    global website
    website = "asdf.com"
    print("Dentro de la función ", website)
holaMundo()

print("Imprimiendo desde fuera de la función", website)

#Funciones pre definidas - Las que son existentes del lenguaje.

#Funciones generales
nombre = "Jose"
print(type(nombre))

#Detectar tipado
comprobar = isinstance(nombre, str)
if comprobar:
    print("Esa variable es un string")
else:
    print("No es un string")

if not isinstance(nombre, float):
    print("La variable no es un float")

#Limpiar espacios
frase = "         mi contenido  "
print(frase.strip())

year = 2022
print(f'holaa {year}')
del year
#print(year)

texto = "  fff  "
if len(texto) <= 0: #la variable estyaría vacía
    print("La variable está vacía")
else:
    print(f"La variable tiene ", len(texto))

#Encontrar caracteres
frase = "La vida es bella"  #en que lugar de la cadena empieza la palabra
print(frase.find("vida"))

#Reemplazar palabras en un string
nueva_frase = frase.replace("vida", "moto") #cual quier sustituir / por
print(nueva_frase)

#Mayúsculas y minúsculas
print(frase.lower())
print(frase.upper())

#Recomendación usar return y hacer el print por fuera

def mi_funcion (nombre):
    return "Hola que tal " + nombre  #las variables tienen que estar definidas antes de invocar la función

def mi_funcion2 (apellido):
    print("Como estás " + apellido)

nombre = "Jose"
apellido = "Lascar"

print("Hola mundo")
print(f"Bienvenido {nombre}")

print(mi_funcion(nombre))
mi_funcion2(apellido)



