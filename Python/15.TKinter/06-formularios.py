from tkinter import *

ventana = Tk()   #creando ventana un objeto Tk
ventana.geometry("700x400")
ventana.title("FORMULARIOS Tkinter | Jose Lascar")


# Texto encabezado
encabezado = Label(ventana, text ="Creando formularios con Tkinter") #encabezado usando un objeto Label
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Calibri",18),
    padx=10,
    pady=10 #que haya un poco mas de espacio entre el texto y los marcos.
)
encabezado.grid(row=0,column=0,padx=5,pady=5, columnspan=15,sticky=W)  #sticky, pégalo a la izquierda con archor
                                            #Son las comunas de espacio que existen en la ventana o frame


#TEXT_BOX NOMBRE
text_box = Entry(ventana) #Usando objeto Entry
text_box.grid(row=1,column=1,padx=5,sticky=W, pady=5)   # para alinear cosas usar el grid en vez del pack, si ya se está usando el PACK genera error
text_box.config(justify="right",state="normal")
#LBL TEXT_BOX NOMBRE
lbl = Label(ventana, text="Nombre")
lbl.grid(row=1,column=0,padx=5,pady=5, sticky=W)


#TEXT_BOX APELLIDO
text_box = Entry(ventana) 
text_box.grid(row=2,column=1,padx=5, sticky=W, pady=5) 
text_box.config(justify="left",state="normal")
#LBL APELLIDO
lbl = Label(ventana, text="Apellido")
lbl.grid(row=2,column=0,padx=5,pady=5,sticky=W)

#LBL DESCRIPCIÓN
lbl = Label(ventana, text="Descripción")
lbl.grid(row=3,column=0,sticky=N,padx=5,pady=5)
# TEXT_BOX DESCRIPCIÓN
textb_grande = Text(ventana)   #Usando objeto TEXT
textb_grande.grid(row=3,column=1)
textb_grande.config(
    width=30, 
    height=5,
    font=("calibri",12),
    padx=5,
    pady=5
    ) #configurando tamaño de la box


# C R E A R  B O T O N E S  (Obtejo Button)


Label(ventana).grid(row=4,column=1) #Separación

btn = Button(ventana, text="Enviar")
btn.grid(row=5,column=1, sticky=E)
btn.config(
    padx=10,
    pady=10,
    bg="lightblue",
    fg="black"

)



ventana.mainloop()