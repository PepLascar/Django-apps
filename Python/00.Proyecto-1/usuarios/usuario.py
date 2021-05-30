#archivo con métodos para crear objetos usuario.
import mysql.connector
from datetime import date
import hashlib



import usuarios.conexion as con   #cuando ya estoy dentro del módulo importo así.

connect = con.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:
    def __init__(self, nombre, apellido, mail, clave):
        self.nombre = nombre    #Entregándole los parámetros al constructor.
        self.apellido = apellido
        self.mail = mail
        self.clave = clave

    def registrar(self):

        cifrar = hashlib.sha256() #Cifrar constraseña.
        cifrar.update(self.clave.encode('utf8')) #tengo que entregar los datos de la clave cifrada.

        fecha = date.today()   #podría importar la fecha actual
        sql = "INSERT INTO usuarios VALUES(null, %s,%s,%s,%s,%s)"   # %s es para sustituir datos que tengo en una tupla.
        usuario = ( self.nombre, self.apellido, self.mail, cifrar.hexdigest(), fecha)

        try:
            cursor.execute(sql, usuario)
            database.commit()
            return [cursor.rowcount, self]  #lista con cantidad de usuarios y retornar su objet con los datos.

        except:
            result = [0, self]  #aquí voy a capturar el error/excepción
        
        return result


    def identificar(self):  
        #Consulta para comprobar si existe usuario.      
        sql = "SELECT * FROM usuarios WHERE mail = %s AND password = %s"

        
        cifrar = hashlib.sha256() #Cifrar constraseña.
        cifrar.update(self.clave.encode('utf8')) #tengo que entregar los datos de la clave cifrada.
        
        usuario = (self.mail, cifrar.hexdigest())

        cursor.execute(sql, usuario)
        resultado = cursor.fetchone()
        return resultado
