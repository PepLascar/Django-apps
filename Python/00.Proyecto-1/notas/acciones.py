
import notas.nota as modelo
from notas import nota as modelo


class Acciones:

    def crear(self, usuario):
        print(f'\n Ok {usuario[1]} vamos a crear una nueva nota.')

        titulo      = input("Titulo de la nota: ")
        descripcion = input("Escribe el contenido de la nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar [0] >= 1:
            print(f"\n Has guardado la nota: {nota.titulo}")
        else:
            print(f'No se ha guardado la nota, lo siento {usuario[1]}')

        return None

    def mostrar(self, usuario):

        print(f"Entendido {usuario[1]}! Aquí tienes tus notas: ")
        nota  = modelo.Nota(usuario[0], "","")
        notas = nota.listar()

        for i in notas:

            print(f"\n******** Notas ********")
            print(i[2])
            print(i[3]) #índice donde están las notas.
            print("----------------------------------")

    def borrar(self, usuario):
        print(f"\n Bien {usuario[1]}, vamos a borrar las notas!")

        titulo = input("Titulo nota a borrar: ")
        nota = modelo.Nota(usuario[0], titulo,"")
        eliminar = nota.eliminar()

        if eliminar[0] >= 1: #Si ha modificado la fila 
            print(f'Hemos borrado la nota {nota.titulo}')
        else:
            print("No se ha borrado la nota. Intente denuevo.")

        return None