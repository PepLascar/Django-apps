import os
os.system('cls')
from usuarios import acciones

print("""
    MENÚ
    - 1. Registro
    - 2. Login
""")

hacer = acciones.Acciones()  #importo modulo/objeto: Acciones
accion = int(input("Que acción desea realizar: "))

if accion == 1:
    hacer.registro()  #importo def registro con el objeto hacer tipo acciones

elif accion == 2:
    hacer.login()

else:
    print("ELSE")


