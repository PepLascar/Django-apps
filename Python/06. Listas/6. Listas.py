import os
os.system("cls")

"""
Lista (Array) Son colecciones o conjuntos de datos/valores, bajo un único nombre.
Para acceder a esos valores podemos usar un índice númerico.
"""

#definir lista
lista_peliculas = ["Batman", "IronMan", "Spiderman"]   #Índice 0,1,2 ... ...

#definir lista con list (Lo mismo que una lista pero los elementos no se pueden modificar)
cantentes = list(("2pac", "drake", "biggie"))
years = list(range(2020,2030))
lista_variada = ["Jose", 31, True, 0.1]

"""
print(lista_peliculas)
print(cantentes) #ahora los elementos serían modificables
print(years)
print(lista_variada)
"""
#Indices para acceder a los elementos en una lista 
print(lista_peliculas[0:7])
print(lista_peliculas[1:])   #sacar todos los elementos a partir del índice 1
#print(lista_peliculas[-1])
#print(lista_peliculas[3])

#Modificando índices
lista_peliculas[1] = "Ganster Americano"
print(lista_peliculas[0:])

cantentes.append("zatu")
print(cantentes)

#RECORRER Y MOSTRAR LISTAS
nueva_pelicula = ""
while nueva_pelicula != "a" :
    nueva_pelicula = input("Introducir nueva película: ")

    if nueva_pelicula != "parar":
        lista_peliculas.append(nueva_pelicula)

for i in lista_peliculas:
    print(f'Pelicula: {lista_peliculas.index(i)+1}. {i}')


#LISTAS MULTIDIMENSIONALES

print("")

contactos = [
    [
        'Antonio',
        'antonio@cl'
    ],
    [
        'Luis',
        'luis@luis.cl'
    ],
    [
        'Mat',
        'mat@mat.cl'
    ]

]

#print(contactos[1])  #accedo a la lista a través del índice

for i in contactos:
    for x in i:
        if i.index(x) == 0:
            print("Nombre: " + x)
        else:
            print("Mail: " + x)
            #print(f'{x}')
    print("\n")