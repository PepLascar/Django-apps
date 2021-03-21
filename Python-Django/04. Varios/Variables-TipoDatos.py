import os
os.system("cls")

#Comentar bloque
"""
print('holamundo')
d = 1
x = 99
print(d+x)
"""

#Python reconoce el tipo de dato de la variable (No pueden comenzar con número)
edad = 31
texto = "Variable de texto"
altura = 1.59
tipoDatoNada = None
flag = True
lista = [1,2,3,4,5,6,7,8,9]
tupla = ("Probando","La","Tupla")#Lista de datos que no cambia
rango = range(9)
diccionario = {
        "Nombre": "Jose",
        "Apellido": "Lascar",
        "Edad": edad
}

#Revisando tipo de satos
print(type(tipoDatoNada))
print(type(texto))
print(type(edad))
print(type(altura))
print(type(flag))
print(type(lista))
print(type(tupla))
print(type(diccionario))
print(type(rango))
print("")

#Concatenación
nombre   = "Jose"
apellido = "Lascar"
print(f'{nombre} {apellido}\nEdad: {edad}\nAltura: {altura}\n')
print("Concat con format \n{}\n{}\n{}\n{}".format(nombre, apellido, edad, altura)) #Contact con parametros en el print

#Convertir tipo de dato (No se puede concat str + int)
texto1 = str(100)
texto2 = str(999)
var3   = float(8)
var4   = 12
var5   = var3 + var4
textt  = texto1 +"\n"+ texto2 + "\t"+ texto1
print(f'{var4+var3} {texto1}')
print(var5)
print(textt)

#Operadores aritméticos. Si el resultado es exacto muestra 0, si el resultado de la división es PAR o IMPAR
num1 = 60
num2 = 3
resto = num1 % num2
print('el resto es', resto)


#variable =   0
#variable +=  5   suma 5 a lo que contiene la variable
#variable -=  5   resta 5 a la variable

#var = 2021
#var = var + 1
#var = var + 1