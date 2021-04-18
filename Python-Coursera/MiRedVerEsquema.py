import os
os.system('cls')
lista_usuarios=[]
flag = True

while(flag==True):
    print("Bienvenido a")
    print("""
                _                  __
    ____ ___  (_)  ________  ____/ /
    / __ `__ \/ /  / ___/ _ \/ __  /
    / / / / / / /  / /  /  __/ /_/ /
    /_/ /_/ /_/_/  /_/   \___/\__,_/

    """)

    usuario = input("Para empezar, dime como te llamas.\nTu nombre: ")
    print(f"\n¡Hola {usuario}!, Bienvenido a Mi Red.\n")
    lista_usuarios.append(usuario)

    año = int(input("Para preparar tu perfil, dime en que año naciste: \n"))
    edad = 2020-año

    estatura = float(input("Cuéntame más de ti, para completar tu perfil. ¿Cúanto mides?(en metros) "))
    estatura_m = int(estatura)
    estatura_cm = int( (estatura - estatura_m)*100 )
    pais = input("¿Cual es tú país? ")
    num_amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes: "))

    print()
    print("Muy bien,", usuario, ". Entonces vamos a crear un perfil con tus datos.")
    print("--------------------------------------------------")
    print("Nombre:  ", usuario)
    print("Edad:    ", edad, "años")
    print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
    print("País:    ", pais)
    print("Amigos:  ", num_amigos)
    print("--------------------------------------------------")
    print("Gracias por la información. Esperamos que disfrutes con Mi Red.")
    print()

    mensaje = input("¿Qué piensas hoy?... ")
    print("--------------------------------------------------")
    print(usuario, "dice:", mensaje)
    print("--------------------------------------------------")

    continuar = True
    while continuar:
        escribir_mensaje = str(input("¿Deseas escribir otro mensaje? (S/N) ")).upper()

        if escribir_mensaje == "S":
            mensaje = input("¿Qué más piensas hoy?... ")
            print()
            print("--------------------------------------------------")
            print(lista_usuarios[0], "dice:", mensaje)
            print("--------------------------------------------------")

        elif escribir_mensaje == "N":
            continuar = False
        
        else: 
            print("Escriba opción válida")
        
        #SALIDA DE LA RED
    print(f"USUARIOS REGISTRADOS:", len(lista_usuarios), lista_usuarios)
    continuar = input("¿Desea registrar un nuevo usuario? S/N").upper()
    if(continuar=="S"):
        flag = True
    else:
        flag = False
        print("¡Vuelve pronto!")
    
