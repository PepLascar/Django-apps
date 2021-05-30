#Esta clase va a manejar las acciones que se pueden realizar en torno a manipular Notas.
from datetime import date

from usuarios import conexion as con
connect = con.conectar()
database = connect[0]
cursor = connect[1]

#import usuarios.conexion as con



class Nota:
    #Crear el constructor, forma de la cual le voy a dar valores a estar propiedades
    def __init__(self, usuario_id, titulo, descripcion):  #pasamos usuario, titulo y descripción, por que la ID y Fecha se   completan automaticamnente.
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    def guardar(self):

        sql  = "INSERT INTO notas VALUES(null, %s,%s,%s,NOW())"
        nota = (self.usuario_id, self.titulo, self.descripcion)

        cursor.execute(sql, nota)
        database.commit()

        return [cursor.rowcount, self] #cantidad de registro afectados del objeto


    def listar(self):

        sql = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id}"
        cursor.execute(sql) #ejecuto mi consulta.
        result = cursor.fetchall()
        return result

    # MEJORA, BORRAR NOTA POR TÍTULO
    def eliminar(self):  
        sql = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%'"  #cuando el titulo esté contenido ...
        cursor.execute(sql)
        database.commit()  #guardar los cambios

        return [cursor.rowcount,self]