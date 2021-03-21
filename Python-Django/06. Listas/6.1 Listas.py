cantantes = ['2pac','Zatu','Leo Rey','Bad bunny']
numeros   =[1,2,5,8,3,4]

#Ordenar una lista
print(numeros)
numeros.sort()
print(numeros)

#Dar vuelta
numeros.reverse()
print(numeros)

#Añadir
cantantes.append("Mago de oz")   #agrega elemento al final de la lista.
print(cantantes)

#Insertar
cantantes.insert(3, "Biggie")    #inserta un elemento en el index indicado, se reemplaza.
print(cantantes)

#Eliminar elementos              #eliminar un elemento/índice
cantantes.pop(4)
cantantes.remove('Leo Rey')      #eliminar por lo que contiene el índice.
print(cantantes)

#Buscar 
print('Drake' in cantantes)

#Contar
print(len(cantantes))    #imprimir largo de la lista

#Cúantas veces se repite un elemento Contar
numeros.append(8)
print(numeros.count(8))

#Buscar un índice en específico (En que índice se encuentra)
print(cantantes.index('Zatu')) 

#Unir listas (a cantantes de le va a unir números)
cantantes.extend(numeros)
print(cantantes)
