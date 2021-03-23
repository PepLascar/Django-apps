#FRAMES: CAJAS DENTRO DE LA VENTANA - VENTANA DENTRO DE UNA VENTANA QUE PUEDO MANIPULAR INDEPENDIENTEMENTE

from tkinter import *

ventana = Tk()
ventana.title("Tkinter | FRAMES")
ventana.geometry("700x700")


#MARCO TOP
marco_top = Frame(ventana, width=250, height=250)
marco_top.config(
    #bg='gray'
)
marco_top.pack(side=TOP, anchor=N, fill=X, expand=YES)

#BLUE
marco = Frame(marco_top, width=250, height=250)
marco.config(
    bg='blue',
    bd=3, #borde cambiendo el numero se enancha o engroza
    relief='solid' #flat, groove, raised, ridge, solid, sunken
)
marco.pack(side=LEFT, anchor=NW)

#YELLOW
marco = Frame(marco_top, width=250, height=250)
marco.config(
    bg='yellow',
    bd=3, #borde cambiendo el numero se enancha o engroza
    relief='solid' #flat, groove, raised, ridge, solid, sunken
)
marco.pack(side=RIGHT, anchor=NE)
marco.pack_propagate(False) #para que el marco no se contraiga y se le pueda meter información.
Label(marco, text="Primer marco").pack(side=LEFT, anchor=SE) #primero ubicarlo con elside y luego con el anchor


#MARCO BOTTOM
marco_bottom = Frame(ventana, width=250, height=250)
marco_bottom.config(
    #bg='lightblue'
)
marco_bottom.pack(side=BOTTOM, anchor=S, fill=X, expand=YES)

#RED
marco = Frame(marco_bottom, width=250, height=250)
marco.config(
    bg='red',
    bd=3, #borde cambiendo el numero se enancha o engroza
    relief='solid' #flat, groove, raised, ridge, solid, sunken
)
marco.pack(side=LEFT, anchor=SW)


#GREEN
marco = Frame(marco_bottom, width=250, height=250)
marco.config(
    bg='green',
    bd=3, #borde cambiendo el numero se enancha o engroza
    relief='solid' #flat, groove, raised, ridge, solid, sunken
)
marco.pack(side=RIGHT, anchor=SE)

ventana.mainloop()
