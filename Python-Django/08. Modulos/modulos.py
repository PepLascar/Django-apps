import os
os.system("cls")

#docs.python.org/3/library

#FECHAS
"""
import datetime
print(datetime.date.today())

fecha_completa = datetime.datetime.now()
print(fecha_completa)

print(fecha_completa.year)

fechaPer = fecha_completa.strftime("%d/%m/%y  %H:%M:%S")  #dar formato a la fecha
print(fechaPer  )

print(datetime.datetime.now().timestamp())
"""


#MATEMÁTICAS

import math
print("Raíz cuadrada de 10: ", math.sqrt(10))  #Fn para raíz cuadrada
print("Número Pi: ", float(math.pi))

print("Redondear ", math.floor(6.797949) )
print("Redondear ", math.ceil(6.797949) )


#RANDOM

import random
print("")
print(f"Imprimiendo número aleatorio entre 15 y 67: {random.randint(15,67)} ")