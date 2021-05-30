from tkinter import *
ventana = Tk()
ventana.geometry("700x400")
ventana.title("Ventana para obtener datos")
ventana.config(
    bd=50,
    bg="#ccc",
)

#debo usar una DEF para asignar la información a las variables
def getDato():
    resultado.set(dato.get())   #así voy a recoger el valor de la variable DATO

    if len(resultado.get()) >= 1:
        txt_obtenido.config(
            bg="green",
            fg="white"

            )
    else:
        txt_obtenido.config(
            bg="red",
            fg="white"
            )

dato = StringVar() #variable para asignarle valor a var DATO
resultado = StringVar()

Label(ventana, text="Ingresa un texto").pack(anchor=NW)
Entry(ventana, textvariable=dato).pack(anchor=NW)  #Box para ingresar datos.   TEXTVARIABLE = guardar datos en variables. En esta entrada tengo que usar la def para asignar el valor

Label(ventana, text="Dato obtenido").pack(anchor=NW)
txt_obtenido = Label(ventana, textvariable=resultado)

txt_obtenido.pack(anchor=NW) #si pongo solo text no funciona

Button(ventana, text="Mostrar", command=getDato).pack(anchor=NW)   #usar command=getDato = cuando haga click se ejecuta def getDato

ventana.mainloop()