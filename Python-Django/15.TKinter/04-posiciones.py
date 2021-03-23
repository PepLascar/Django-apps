from tkinter import *

ventana = Tk()
#ventana.geometry("500x500")

def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos} del pais {pais}"

#VENTANA : BIENVENIDO AL PROGRAMA
texto = Label(ventana, text = "Bienvenidos al programa")
texto.config(
            fg='white',
            bg='#000000',
            padx=20,
            pady=20,
            font=('Calibri', 30)

)
texto.pack(side=TOP) #left right o bottom


#VENTANA 2 : SOY JOSE LASCAR
texto = Label(ventana, text = pruebas(nombre="Jose",apellidos="Lascar", pais="Chile"))
texto.config(
    #width=500,
    height= 3,
    justify=RIGHT,
    bg='orange',
    font=('Arial',18),
    cursor='cross'
)
texto.pack(side=TOP, fill=X, expand=YES)


#VENTANA A
texto = Label(ventana, text = "VENTANA A")
texto.config(
    bg="red",
    font=('Arial',18),
    padx=10,
    pady=20
)
texto.pack(side=LEFT, fill=X, expand=YES)

#VENTANA B
texto = Label(ventana, text = "VENTANA B")
texto.config(
    bg="blue",
    font=('Arial',18),
    padx=10,
    pady=20
)
texto.pack(side=LEFT, fill=X, expand=YES)

#VENTANA C
texto = Label(ventana, text = "VENTANA C")
texto.config(
    bg="green",
    fg="white",
    font=('Arial',18),
    padx=10,
    pady=20
)
texto.pack(side=LEFT, fill=X, expand=YES)


ventana.mainloop()

