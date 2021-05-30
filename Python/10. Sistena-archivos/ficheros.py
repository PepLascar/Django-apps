import os
os.system("cls")

#Trabajando con ficheros y directorios.

from io import open
import pathlib
import shutil #copiar, renombrar y eliminar archivos.


# Abrir archivo
#archivo = open("10.Sistena-archivos/fichero_text.txt", "a+")  #a+ es crear en el caso que no exista
ruta = str(pathlib.Path().absolute()) + "/fichero_text.txt"
#archivo = open(pathlib.Path.absolute() + "fichero_text.txt", "a+")  #a+ es crear en el caso que no exista
print(ruta)
archivo = open(ruta, "a+")


#Escribir
archivo.write("***TEXTO INGRESADO DESDE PYTHON***\n")


#Cerrar archivo
archivo.close()


#Abrir
ruta = str(pathlib.Path().absolute()) + "/10.Sistena-archivos/fichero_text.txt"
print(ruta)
archivo_lectura = open(ruta, "r")



#LEER CONTENIDO
#contenido = archivo_lectura.read()
#print(contenido)

#Leer contenido y guardarlo dentro de una variable lista.
lista = archivo_lectura.readlines()
archivo_lectura.close()
print(lista)

for frase in lista:
    # if not frase.isnumeric():  se pueden validar diferentes elementos
    lista_frase = frase.split()
    print(lista_frase)
    #print("- "+frase.upper())


#COPIAR de un fichero a otro    KMLMJ,JHGYYGGGGGFCSDZXXXWEASRSAYT
ruta_original = str(pathlib.Path().absolute()) + "/10.Sistena-archivos/fichero_text.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/10.Sistena-archivos/fichero_copiado.txt"
ruta_alternativa = str(pathlib.Path().absolute()) + "/06. Listas/fichero_copiado88.txt" #agregar ruta alternativa a otra caerta
shutil.copyfile(ruta_original, ruta_nueva)
#shutil.copyfile(ruta_original, ruta_alternativa)


#Fichero copiado y renombrado
ruta_original = str(pathlib.Path().absolute()) + "/10.Sistena-archivos/fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/10.Sistena-archivos/fichero_copiado_NUEVO.txt"
shutil.move(ruta_original, ruta_nueva)


#Eliminar
os.remove(ruta_nueva)

#Comprobar si existe un archivo
#print(f'Imprimiendo path {os.path.abspath("./")}')  #.. es el anterior

comprobar_ruta = os.path.abspath("./") + "../fichero_text.txt"
print(f'Comprobando ruta archivo {comprobar_ruta}')

if os.path.isfile(comprobar_ruta):
    print('El archivo existe')
else:
    print("El archivo no existe")


