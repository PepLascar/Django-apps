import os
os.system("cls")

#Crear lista con 8 números
#Recorrer lista y mostrarla
#Ordenarla y mostrarla
#Mostrar su longitud
#Buscar algún elemento que el usuario indique

lista = [3,2,9,8,7,4,1,6]
for i in lista:
    print(f'{i}')


print(f'La lista tiene: {len(lista)} elementos')


buscar = int(input('Ingrese número a buscar'))

comprobar = isinstance(buscar, int)
while not comprobar or buscar <= 0:
    buscar = int(input("Volver a introducir número: "))
else:
    print(f'Has introducido para buscar el índice: {buscar}')

#search =  lista.index(buscar)
print(f'El elemento buscado se encuentra en la posición: {lista.index(buscar)}') 


def mostrar_lista(listar):
    resultado = ""

    for elemento in listar:
        resultado += "Elemento " + str(elemento)
        resultado += "\n"
    return resultado


lista.sort()
print(mostrar_lista(lista))


# Ejercicio 2
# Añadir valores a una lista mientras su lngitud sea < 120 y luego mostrar la lista
# Usar while y for

coleccion = []
for cont in range (0,120):
    coleccion.append(f'Índice - {cont+1}')
    print("Mostrando el: " + coleccion[cont])

colect = []    
x = 0
while x < 120:
    colect.append(f'Elemento: {x+1}')
    print("Mostrando: " + colect[x])
    x += 1



lista      = [ ]
listaWhile = [ ]

contador = 0

if len(lista) < 120:
    for i in range(120):
        lista.append("u")

print(lista)
print(f'Largo lista: {len(lista)}')


contador = 0

while contador < 120:
    listaWhile.append("J")
    contador += 1
print(listaWhile)
print(f'Largo lista: {len(listaWhile)}')



# Ejercicio 3: Comprobar si una variable está vacía. Si lo está, rellenarla con un texto en minúsculas y mostrarlo en mayúsculas.

texto = ""

if len(texto.strip())  <= 0:
    texto = "texto"
    print(texto.upper())

else:
    print(f'La variable tiene contenido: {texto}')


# Ejercicio 4 : Crear un script que tenga 4 variables
# Una lista, un string, un int y un bool --> Y que imprima un mensaje según el tipo de dato de cada variable . Usar funciones

def tipoDato(tipo):
    result = None
    if tipo   == list:
        result = "Lista"
    elif tipo == str:
        result = "String"
    elif tipo == int:
        result = "Entero"
    elif tipo == bool:
        result = "Booleano"
    else:
        result = "Es otro tipo de dato"

    return result


def comprobarTipo(dato, tipo):
    test   = isinstance(dato, tipo)
    result = ""

    if test:
        result = f'Dato del tipo: {tipoDato(tipo)}'
    else:
        result = f'No es del tipo de dato inducado: {type(dato)}'

    return result

lista  = []
string = "Hola"
numero = 8
flag   = True

print(comprobarTipo(lista, list))

# Ejercicio 5:
# Crear una lista con el contenido de esta tabla:
# Mostrar esta información ordenada ... mostrar categoría acción ... luego aventura ... luego deporte

juegos = [
    {
        "Categoría": "ACCIÓN + ",
        "Juegos": ["GTA", "COD", "PUBG"]
    },
    {
        "Categoría": "AVENTURA + ",
        "Juegos": ["Asassin","Crash","Mario"] 
    },
    {
        "Categoría": "DEPORTES + ",
        "Juegos": ["FIFA 21","NFL 21","Moto gp"]
    },

]
#print(type(juegos))

for i in juegos:
    print(f"\nCategoría: {i['Categoría']}")
    for x in i['Juegos']:
        print(f"{x}")
