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
        infoServer = conexion.get_server_info()
        print(f"Información del servidor: {infoServer}")
        
except Error as ex:
    print("Error durante la conexión.")

finally:    #siempre se ejecuta independiente de que haya ahbido exito o no
    if conexion.is_connected():
        conexion.close()
        print("Acción finalizada")



""" EJEMPLO 
import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='pynative',
                                         password='pynative@#29')

    mySql_Create_Table_Query = ""CREATE TABLE Laptop ( 
                             Id int(11) NOT NULL,
                             Name varchar(250) NOT NULL,
                             Price float NOT NULL,
                             Purchase_date Date NOT NULL,
                             PRIMARY KEY (Id)) ""

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Laptop Table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
"""