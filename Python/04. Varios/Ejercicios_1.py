import os
os.system("cls")

# Ejercicios Round 1

# Ejercicio 1
from datetime import date

pais = 'Chile'
continente = 'América del Sur'
hoy = date.today()

print(f'El país {pais} se encuentra en el continente {continente}')
print(f'Día de consulta: {hoy}')
print(type(pais))
print(type(continente))


#Ejercicio 2

par = 0
for i in range(1,51):
    par = i * 2
    print(par)

for par in range (1,100):
    if par%2 == 0:   #estoy sacando los que son par con el numeral
        print(par)
    else:
        print('----')


#Ejercicio 3

cont = 0
for i in range (1,61):
    cont = i**2
    print(cont) 


flag = 0
while flag <= 59:
    flag += 1
    print(f'El cuadrado de {flag} es {flag**2}')



#Ejercicio 4

ope = int(input('¿Qué operación desea realizar?\n1. SUMAR \n2. RESTAR \n3. MULTIPLICAR \n4. DIVIDIR\n'))

num1 = int(input('Primer número a operar: '))
num2 = int(input('Segundo número a operar: '))

if ope == 1:
    print(F'{num1 + num2}')
elif ope == 2:
    print(F'{num1 - num2}')
elif ope == 3:
    print(F'{num1 * num2}')
elif ope == 4:
    print(F'{num1 / num2}')
else:
    print('f i n    d e l   p r o g r a m a')


#Ejercicio 5

inicio = int(input('¿Desde que número deseas mostrar?: '))
fin    = int(input('¿Hasta que número deseas mostrar?: '))

if inicio < fin :

    for i in range(inicio, (fin+1)):
        print(f'{i}')
else:
    print('El primer número tiene que ser menor al del fin.')



#Ejercicio 6

num_user  = 0

for i in range(0,10):
    num_user += 1
    print(f'\n## Tabla del {num_user} ##')

    cont = 1
    while cont <= 10:
        print(f'{num_user} x {cont} = {num_user * cont}')
        cont += 1
else:
    print('\nPrograma finalizado')



#Ejercicio 7

inicio = int(input('¿Desde que número deseas mostrar?: '))
fin    = int(input('¿Hasta que número deseas mostrar?: '))

if inicio < fin :


    for i in range(inicio, fin):
        if i%2 == 1:
            print(f'{i}')


else:
    print('El primer número tiene que ser menor al del fin.')



#Ejercicio 8

porcentaje = int(input('Ingrese porcentaje que quiere obtener: \n'))
numero     = int(input('¿A que número?: \n '))
total = 0

print(F'¿ Cúanto es el {porcentaje}% de {numero} ?')
total = numero * (porcentaje/100)
print(f'El {porcentaje}% de {numero} es {round(total)}')



#Ejercicio 9

numero = 0
while numero != 111:
    numero = int(input('Ingrese número: \n'))
print('Ingresaste el número correcto, puedes salir del programa.')


        
#Ejercicio 10

cont = 1
aprobados = 0
suspendidos = 0

alumno = int(input('¿Cantidad de alumnos del curso?: \n'))

while cont <= alumno:
    nota = int(input(f"Nota alumno {cont} | "))

    if nota >= 40:
        aprobados += 1
    else:
        suspendidos += 1

    cont += 1

print(f'Aprobados  {aprobados} \nRepitentes  {suspendidos}')


