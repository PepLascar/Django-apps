
#MENU
lista_usuarios = []

flag = True
while(flag== True):
    try:
        print("----------------------------------------------")
        opcion = int(input("\nMENÚ Ingrese una opción:\n1) REGISTRAR\n2) EDITAR\n3) MOSTRAR.\n4) SALIR.\n---------------\nIngrese opción: "))
    except ValueError:
        print("Ingrese opción válida.")

    if(opcion==1):
        print("REGISTRAR")
        usuario = input("Para empezar, dime como te llamas.\nTu nombre: ")
        print(f"\n¡Hola {usuario}!, Bienvenido a Mi Red.\n")
        lista_usuarios.append(usuario)

    if(opcion==2):
        editar_usuario = int(input("Ingrese usuario a editar"))
        lista_usuarios.pop(editar_usuario)
        usuario = input("Ingrese nuevo usuario")
        lista_usuarios.append(usuario)

    if(opcion==3):
        print("MOSTRAR")
        print(f"USUARIOS REGISTRADOS:", len(lista_usuarios), lista_usuarios)

    if(opcion==4):
        print("SALIR")
        flag = False
        print("Saliste del menú")

    continuar = input("¿Desea continuar usando la aplicación? S/N").upper()
    if(continuar=="S"):
        flag = True




print("Bienvenido a ... ")
print("""
              _                  __
   ____ ___  (_)  ________  ____/ /
  / __ `__ \/ /  / ___/ _ \/ __  /
 / / / / / / /  / /  /  __/ /_/ /
/_/ /_/ /_/_/  /_/   \___/\__,_/

""")

# Solicitud de nombre
nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()

agno = int(input("Para preparar tu perfil, dime en quÃ© aÃ±o naciste. "))
edad = 2017-agno-1
print()

estatura = float(input("CuÃ©ntame mÃ¡s de ti, para agregarlo a tu perfil. Â¿CuÃ¡nto mides? DÃ­melo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )

num_amigos = int(input("Muy bien. Finalmente, cuÃ©ntame cuantos amigos tienes. "))

print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "aÃ±os")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centÃ­metros")
print("Amigos:  ", num_amigos)
print("--------------------------------------------------")
print("Gracias por la informaciÃ³n. Esperamos que disfrutes con Mi Red")
print()

continuar = True

while continuar:

    escribir_mensaje = str(input("Â¿Deseas escribir un mensaje? (S/N) "))

    if escribir_mensaje == "S" or escribir_mensaje == "s" or escribir_mensaje == "":
        mensaje = input("Vamos a publicar un mensaje. Â¿QuÃ© piensas hoy? ")
        print()
        print("--------------------------------------------------")
        print(nombre, "dice:", mensaje)
        print("--------------------------------------------------")
    else:
        continuar = False












