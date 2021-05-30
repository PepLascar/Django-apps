import os
os.system("cls")

import sqlite3

#Conexión
conexion = sqlite3.connect('pruebas.db')  #Aquí se va a almacenar la base
#conexion = sqlite3.connect('00.Proyecto-1/base.db')  #Ruta que se va a almacenar la base

#Crear  cursor
cursor = conexion.cursor()

#Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(100),
    descripcion text,
    precio int(10)
);
""")

#Guardar cambios
#conexion.commit()

#Insertar datos
#cursor.execute("INSERT INTO productos VALUES (null, 'Segundo prod', 'Descripcion producto', 550 )")

# Listar datos
cursor.execute("SELECT * from productos WHERE precio >= 700;")
productos = cursor.fetchall()
print(productos)

for i in productos:
    print("id: ", i[0])
    print("Titulo: ", i[1])
    print("Descripcion: ", i[2])
    print("Precio: ", i[3])
    print("\n")

cursor.execute("SELECT titulo from productos;")
producto = cursor.fetchone()  #sacando primer registro de la tabla
print(producto)

#Borrar registros
cursor.execute("DELETE FROM productos")
#Guardar cambios
conexion.commit()

#Insertar VARIOS registros
productos = [
    ("Notebook", "Acer", 750),
    ("Celular", "Samsung", 650),
    ("Consola", "Nintendo", 850),
    ("Tablet", "Mac", 550),
    ("Monitor", "LG", 950)
]

#INSERT
cursor.executemany("INSERT INTO productos VALUES(null,?,?,?)", productos)  #executeMany para ejecutar varias consultas

#UPDATE
cursor.execute("UPDATE productos SET precio = 888 where precio = 550")




#Guardar cambios
conexion.commit()
#Cerrar conexion
conexion.close()

