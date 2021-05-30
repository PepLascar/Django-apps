import os
os.system("cls")

import misModulos #citar en general
from misModulos import holaMundo   #invocar una función definida
from misModulos import *

#nombre archivo del modulo + funcion del modulo + paramétros.
#puedo tener mis funciones y taras guardadas en módulos

print(misModulos.holaMundo("Jose"))
print(calculadora(3,5,True))   #Puedo buscar formas de no anteponer el nombre del módulo y usarlo directamente.

print(holaMundo("Pep coding"))



