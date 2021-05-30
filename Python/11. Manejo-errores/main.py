import os
os.system("cls")
#Controlar errores y excepciones para capturarlos y procesarlos de mejor manera para el usuario.
#Capturar excepciones y manejar errores en código susceptible a fallos/errores

#NameError - excepción
#ValueError - 
#Traceback
#Type error


try:
    nombre = input("Cúal es tu nombre ? ")


    if len(nombre) > 1:
        nombre_usuario = "El nombre es " + nombre


    print(f'{nombre_usuario}')
except:
    print("Ha ocurrido un error, dige bien el nombre.")
else:
    print("Nombre de usuario correcto!")

finally:  #con esto se detectas cuando termina el bloque try. Siempre se va a ejecutar al final
    print("Fin de la iteración Try-Except")

#-------------------------------------------------------------------------------------------------
"""
lista = [3,2,9,8,7,4,1,6]
for i in lista:
    print(f'{i}')
print(f'La lista tiene: {len(lista)} elementos')

try:
    buscar = int(input('Ingrese número a buscar'))

    comprobar = isinstance(buscar, int)
    while not comprobar or buscar <= 0:
        buscar = int(input("Volver a introducir número: "))
    else:
        print(f'Has introducido para buscar el índice: {buscar}')


        search =  lista.index(buscar)
        print(f'El elemento buscado se encuentra en la posición: {search}') 
except:
    print("El número no está en la lista. Lo siento.")
    """

#-------------------------------------------------------------------------------------------------
# Multiples excepciones
"""
try:
    numero = int(input("Número para elevarlo al cuadrado"))
    print(f'El cuadrado del número es {numero*numero}')
except TypeError:
    print("Debes convertir el String ingresado a Int.")
except ValueError:
    print("Introduce un valor númerico.")
except Exception as e:
    print(type(e))
    print("Ha ocurrido un error: ", type(e).__name__)   #Le paso el error con la e  .... y con la constante __name__ me muestra el error. Me arroja que tipo de error tengo
"""

#-------------------------------------------------------------------------------------------------
# Personalizadas excepciones o lanzar excepcion   RAISE

try:
    nombre = input("introduce nombre: ")
    edad = int(input("Edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es correcta")
    elif len(nombre) <=1:
        raise ValueError("El nombre no está completo")
    else:
        print(f"Bienvenido a Python {nombre}")
except ValueError:
    print("Introducir datos correctamente.")
except Exception as e:
    print(f"Capturando el tiepo de error")

    