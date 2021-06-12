import mysql.connector, os
from mysql.connector import Error
os.system("cls")

try:
    conexion = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='1234',
        db='base_python'
    )

    if conexion.is_connected():
        print("Conexión exitosa.")
        cursor = conexion.cursor() #cursor para hacer un nexo con la base de datos
        cursor.execute("SELECT database()")
        registro = cursor.fetchone()   #devolviendo registro de la base de datos
        print(f"Conectado a BD: {registro}")
    
        cursor.execute("SELECT * from vehiculos")
        resultado = cursor.fetchall()
        for i in resultado:    #ciclo pra capturar los resultados de la consulta a través de un for
            print(f"\nID: {i[0]}| Marca: {i[1]}| Modelo: {i[2]}| Precio: {i[3]}")
        print(f"\nTotal de registros: {cursor.rowcount}")

except Error as ex:
    print("Error durante la conexión.", ex)

finally:
    if conexion.is_connected():
        conexion.close()
        print("Acción finalizada.")



        