#Tengo que importar MÓDULO(archivo) 
import os
os.system("cls")

from auto import Auto


auto1 = Auto("Amarillo", "Suzuki", "Swift Sport", 100, 1.5, 143)
auto2 = Auto("Verde", "Suzuki", "Vitarat", 90, 1.6, 118)
auto3 = Auto("Negro", "Dodge", "Challenger", 200, 3.0, 520)
auto4 = Auto("Blanco", "Mercedez", "a200", 150, 1.6, 210)

print(f"Información auto: {auto1.getMarca(), auto1.getModelo(), auto1.getColor()} Hp: {auto1.getHp()}\n")

print(auto1.getInfo())  #Imprimiendo información con el método print
print(auto2.getInfo())
print(auto3.getInfo())
print(auto4.getInfo())

#DETECTAR TIPADO
print(type(auto2))

#auto2 = 10
if type (auto2) == Auto:
    print("Es un objeto correcto: Auto")
else:
    print("No es un objeto del tipo auto")

# VISILIBIDAD DE LOS ATRIBUTOS (PÚBLICOS(por defecto) O PRIVADOS). Puede ser accedido/visto fuera o dentro de la clave.
# Usar para limitar o permitir el acceso a atributos dependiendo de lo que se quiera hacer.

print(auto1.soy_publico)   #Se puede acceder
#print(auto1.__soy_privado) #No se puede acceder
print(auto1.getPrivado())