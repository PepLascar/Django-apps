import os
import pathlib
import shutil

# Crear carpeta
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")  #./es para que se cree a partir del directorio actual
else:
    print("Ya existe ese directorio")

# Eliminar carpeta
# os.rmdir('./mi_carpeta')

# COPIAR una carpeta
ruta_original = str(pathlib.Path().absolute()) + "/mi_carpeta"
ruta_nueva = str(pathlib.Path().absolute()) + "/mi_carpeta_copiada"
shutil.copytree(ruta_original, ruta_nueva)

# Eliminar 
os.rmdir('./mi_carpeta_copiada')


# Contar o mostrar archivos con ciclo
print("Contenido de mi carpeta")
contenido = os.listdir('./mi_carpeta')
print(contenido)

for fichero in contenido:
    print("Archivo: " +fichero )