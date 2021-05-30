
from usuarios import usuario as modelo
import notas.acciones 

class Acciones:

    def registro(self):
        print("- Registrarse en el sistema -")
        nombre   = input("Nombre usuario: ")
        apellido = input("Apellido: ")
        mail     = input("Mail de registro: ")
        clave    = input("Ingrese clave: ")

        usuario = modelo.Usuario(nombre, apellido, mail, clave)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre} te has registrado con el correo: {registro[1].mail}")
        else:
            print("No te has registrado correctamente.")
 
    def login(self):
        print('- Conectarse al sistema -')

        try:
            mail  = input("Mail: ")
            clave = input("Clave: ")

            usuario = modelo.Usuario('','',mail, clave)  #creando objeto usuario que recibe mail y clave.
            login   = usuario.identificar()

            if mail == login[3]:
                print(f"\n Bienvenido {login[1]}, te has registrado en el sistema con fecha {login[5]} ")
                self.proximasAcciones(login) # Al método próAcciones le entrego el objeto usuario(login)   #AQUÍ SE ENLAZA CON EL MÉTODO DE REGISTRAR EN NOTAS

        except Exception as e:
            #print(f'\n{type(e)}')
            print(type(e).__name__)
            print("Login incorrecto, inténtalo nuevamente.")

    def proximasAcciones(self, usuario):
        print(""" 
            1. Creat nota 
            2. Mostrar nota
            3. Eliminar nota
            4. Salir 
        """)

        accion = int(input("Ingresar opción: "))
        hacer = notas.acciones.Acciones()   #Llamo al módulo notas para acceder a la clase Acciones.
        if accion == 1:
            hacer.crear(usuario)
            self.proximasAcciones(usuario)
            print("Crear")

        elif accion == 2:
            hacer.mostrar(usuario)     #Siempre entrego los usuarios para trabajar con uno
            self.proximasAcciones(usuario)
            print("Mostrar")

        elif accion == 3:
            hacer.borrar(usuario)
            self.proximasAcciones(usuario)
            print("Eliminar")

        elif accion == 4:
            print("Saliendo ... ...")
            exit()
        else:
            print("Ingresar opción válida.")

        return None
