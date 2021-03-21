contador = 1
while contador <= 30:
    print(f'Estoy en el número: {contador}')
    contador += 1


#Mostrar con while datos tipo string
contador = 1
muestrame = str(0)
while contador <= 30:
    print(f'Estoy en el número: {contador}')
    muestrame = muestrame + ", " + str(contador)
    contador += 1
print(muestrame)


num_user = int(input('Tabla de que número'))

if num_user < 1 :
    num_user = 1

print(f'## Tabla del {num_user} ##')

cont = 1
while cont <= 10:
    print(f'{num_user} x {cont} = {num_user*cont}')
    cont += 1
else:
    print('Tabla terminada')
    

