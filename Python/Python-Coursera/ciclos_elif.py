llueve = True
temperatura = int(input("Ingrese temperatura: "))
if temperatura < 18 and llueve == True:
    print("Llevaré paraguas y abrigo")
elif temperatura < 18 and llueve == False:
    print("Llevaré solo abrigo")
else:
    print("Iré en traje de baño")


#EJERCICIO 2

numero = int(input("Ingrese calidad del aire"))
if numero >= 0 and numero <= 99:
  print("Bueno")
elif numero >= 100 and numero <= 199:
  print("Regular")
elif numero >= 200 and numero <= 299:
  print("Alerta")
elif numero >= 300 and numero <= 499:
  print("Preemergencia")
else:
  print("Emergencia")