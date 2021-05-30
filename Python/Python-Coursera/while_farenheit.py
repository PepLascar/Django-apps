#Autocompletar tabla en celcius
temp = 32
print("f°    c°")
while temp < 73:
    print(temp,"  ", int((temp-32)*5/9))
    temp = temp+1 #condicion que convierte el while en FALSO para salir.

#CONVERTIR FARENHEIT A CELCIUS
celcius   = 0
farenheit = 0

farenheit = int(input("Ingrese grados en Farenheit: "))
celcius = (farenheit - 32) * 5/9
print(round(celcius))
