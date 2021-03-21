"""
OPERADORES DE COMPARACIÓN
== IGUAL
!= DIFERENTE
< MENOR
> MAYOR
>= MAYOR O IGUAL
<= MENOR O IGUAL
AND y
OR  o
!   negación
NOT no
"""

import os
os.system("cls")


print('## EJEMPLO 1 ##')

color = input('Escribe tu color favorito: ')

if color == 'rojo':
    print('Tu color favorito es rojo')
else:
   print('Ese no es tu color favorito')


print('\n## EJEMPLO 2 ##')

anio = int(input('En que año estamos? '))
if anio >= 2021:
    print('Estamos en 2012 o adelante')
else:
    print('No es ese año ')


print('\n## EJEMPLO 3 ##')

edad = int(input('Ingresa tu edad: '))
mayoria_edad = 18
usuario = input('Ingresa tu nombre: ')
registrado = 'si'
if edad >= mayoria_edad:
    print(f'{usuario} Usted es mayor de edad')

    if registrado == 'si':
        print('El usuario está registrado')
        
    else:
        print('El usuario no está registrado')


else:
    print(f'{usuario} Ud. es menor de edad')


print('\n## EJEMPLO 4 ##')
dia = int(input('Ingrese día de la semana: '))

if dia == 1:
    print('Es lunes')
elif dia == 2:
    print('Es martes')
elif dia == 3:
    print('Es miércoles')
elif dia == 4:
    print('Es jueves')
elif dia == 5:
    print('Es viernes')
else:
    print('Es fin de semana')


print('\n## EJEMPLO 5 ##')
ed_min = 18
ed_max = 64
ed_actual = int(input('Ingrese su edad: '))

if ed_actual >= 18 and ed_actual <= 65:
    print('Usted está en edad de trabajar')
else:
    print('No está en edad de trabajar')


print('\n## EJEMPLO 6 ##')

pais = 'Chile'

if pais == 'Mexico' or pais == 'Chile' or pais == 'Perú':
    print(f'El país es de habla hispana!!')


#tener claro de que condición estás entrando en el if o el else
print('\n## EJEMPLO 7 ##')

pais = 'Chile'
#Si no se cumple está condición, que sea lo contrario
if not (pais == 'Mexico' or pais == 'Chile' or pais == 'Perú'):
    print(f'El país es de habla hispana!!')
else:
    print('ELSE')


print('\n## EJEMPLO 8 ##')

pais = 'Chile'
#Si no se cumple está condición, que sea lo contrario
if pais != 'Mexico' and pais != 'Chile' and pais != 'Perú':
    print(f'El país es de habla hispana!!')
else:
    print('ELSE')
    