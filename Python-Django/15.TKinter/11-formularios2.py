from tkinter import *

ventana = Tk()
ventana.geometry("400x300")
ppal = Label(ventana, text="Registro")
ppal.config(
    padx=15,
    pady=15,
    fg="white",
    bg="green",
    font=("consolas",20)
)

ppal.grid(row=0, column=0, columnspan=5, sticky=W)  #creando grilla al label ... pack y row se cae cuando están juntos

Label(ventana, text="¿A que te dedicas?").grid(row=1, column=0, sticky=W)

web = IntVar()
movil = IntVar()  #Aquí se guardarán los datos

def mostrarProfesion():
    texto = ""
    if web.get():
        texto += "Desarrollo Web"


    if movil.get():
        if web.get():
            texto += " y Desarrollo movil"
        else:
            texto += "Desarrollo movil"
    
    mostrar.config(
    text=texto,
    bg="green",
    fg="white"  
    )

mostrar = Label(ventana)
mostrar.grid(row=4, column=0)

#Botones check
Checkbutton(
ventana, 
text="Desarrollo web",
    variable=web,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=2, column=0, sticky=W)

Checkbutton(ventana, 
text="Desarrollo movil",
    variable=movil,
    onvalue=1,
    offvalue=0,  #0 para no marcado
    command=mostrarProfesion
).grid(row=3, column=0, sticky=W)

#Radio Buttons - Vincular los buttons a la variable opción
Label(ventana, text="¿Cual es tu género").grid(row=5,sticky=W)


def marcar():
    marcado.config(text=opcion.get())
    

opcion = StringVar()
opcion.set(None)

Radiobutton(
    ventana, 
    text="Masculino",
    value="Masculino",
    variable = opcion,
    command = marcar
    ).grid(row=6, sticky=W)

Radiobutton(
    ventana, 
    text="Femenino",
    value="Femenino",
    variable = opcion,
    command = marcar
    ).grid(row=7, sticky=W)

Radiobutton(
    ventana, 
    text="Otro",
    value="Otro",
    variable = opcion,
    command = marcar
    ).grid(row=8, sticky=W)

marcado = Label(ventana) #label para mostrar la opción marcada
marcado.grid(row=9, sticky=W)


#OPTION MENU
Label(ventana, text="Selecciona una opción").grid(row=6, column=1)

def seleccionar():
    seleccionado.config(text=opcion.get())
    return None


opcion = StringVar()
opcion.set("Opción 1") #Para tener esta opción por defecto

select = OptionMenu(ventana, opcion, "Opción 1","Opción 2","Opción 3")
select.grid(row=7, column=1)

#Botón para ver la opción seleccionada.
Button(ventana, text= "Ver opción", command=seleccionar).grid(row=8, column=1)

seleccionado = Label(ventana)
seleccionado.grid(row=9, column=1)



ventana.mainloop()
#descargar código clase 146