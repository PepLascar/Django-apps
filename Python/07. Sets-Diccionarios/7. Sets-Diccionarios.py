#DICCIONARIOS - Almacena un conjunto de datos/valores, en vez de tener indices númericos tiene alfanuméricos.
# Un tipo de dato que almacena en formato clave > valor.
import os
os.system("cls")

#Lista con diccionarios
contactos = [
    {
        'nombre': 'antonio',
        'mail': 'antonio@antonio.com',
        'edad': 31
    },
    {
        'nombre': 'luis',
        'mail':'luisito.com',
        'edad': 28
    },
    {
        'nombre': 'pedro',
        'mail': 'pedrito.com',
        'edad': 23
    },   
]

contactos[0]['nombre'] = "Toño"
print(contactos[0]['nombre'])   
#entrando al indice en la lista para luego el índice del diccionarios


for contacto in contactos:
    print(f"Contacto: {contacto['nombre']}")
    print(f"Mail {contacto['mail']}")
    print(f"Edad {contacto['edad']}")
    print("------")


persona = {
    "nombre": "José",
    "apellidos": "Lascar",
    "web": "pep.lascar.com"


}
print(type(persona))
print(persona)

print(persona["apellidos"]) #acceder a un índice

#Lista con diccionarios
contactos = [
    {
        'nombre': 'antonio',
        'mail': 'antonio@antonio.com'
    },

    {
        'nombre': 'luis',
        'mail':'luisito.com'
    },

    {
        'noombre': 'pedro',
        'mail': 'pedrito.com'
    },
        
]

print(contactos)



"""
#SET: Colección de datos que no tienen índice ni orden

personas = {

    "Victor",
    "Pedro",
    "Juan"
}
print(type(personas))
print(personas)

personas.add("Alix")
print(personas)

personas.remove("Pedro")
print(personas)
"""
