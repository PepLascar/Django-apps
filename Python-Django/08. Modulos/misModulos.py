# Forma de empaquetar nuestro código (python modules index  docs.python.org)
# Funcionalidades ya hechas para reutilizar
# Se pueden conseguir, crear o descargar
# Modulos tienen sus métodos

def holaMundo(nombre):
    return f"Hola como estás {nombre}"


def calculadora(num1, num2, basicas = False): #Ese false es prácticamente una Flag
    suma  = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    div   = num1 / num2

    print("\n")
    cadena = ""

    if basicas != False:

        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " +str(resta)
        cadena += "\n"
    else:
        cadena += "Multi: " + str(multi)
        cadena += "\n"
        cadena += "Div: "   + str(div)

    return cadena