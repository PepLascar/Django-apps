cont = 0
for cont in range (0,5):   
    print(f'hola {cont}')

resultado = 0
for cont in range (5):
    resultado += cont   #sumarle a resultado lo que viene después del igual
    print(resultado)



numero_tabla = int(input('De que númmero quieres la tabla: '))
if numero_tabla < -1 :
    numero_tabla = 1

print(f'##La tabla de múltiplicar del número {numero_tabla}##')

for i in range (0,10):

    if numero_tabla == 45 or numero_tabla == 0:
        print('No se puede mostrar esa tabla')
        break

    print(f'{numero_tabla} x {i} = {numero_tabla*i}')
else:
    print(f'Fin del ciclo (else)')
