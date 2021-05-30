from tkinter import *

ventana = Tk()
ventana.geometry("500x500")

#keyword argument
texto = Label(ventana, text = "Bienvenidos al programa")  #Objeto label
texto.config(
            fg='white', #color letra
            bg='#000000', #fondo
            padx=20, # margen eje X
            pady=20, # margen eje y
            font=('Calibri', 30)

)
texto.pack()    #para mostrar el texto debo empaquetarlo en el programa.

def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos} del pais {pais}"



texto = Label(ventana, text = pruebas(nombre="Jose",apellidos="Lascar", pais="Chile")) #parametros de palabra clave
texto.config( #estilos dentro del texto
    #width=500,
    height= 10,
    justify=RIGHT,
    bg='orange',
    font=('Arial',18),
    cursor='cross' #circle, clock, spider
)
texto.pack(anchor=E) #direcciones del texto dentro del pack



texto = Label(ventana, text = "asdf probando segunda ventana")
texto.config(
    height= 300,
    bg="red",
    font=('Arial',18),
    padx=10,
    pady=20
)
texto.pack(anchor=W)
ventana.mainloop()