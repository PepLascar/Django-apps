import mysql.connector, os
from mysql.connector import Error
os.system("cls")

try:
    conexion = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='1234',
        db='flask'
    )

    if conexion.is_connected():
        print("Conexión exitosa.")
        infoServer = conexion.get_server_info()
        print(f"Información del servidor: {infoServer}")
        
except Error as ex:
    print("Error durante la conexión.")

finally:    #siempre se ejecuta independiente de que haya ahbido exito o no
    if conexion.is_connected():
        conexion.close()
        print("Acción finalizada")



"""
flask mysql documentation
flask-mysqldb.readthedocs.io

- pip install flask-mysql

"""