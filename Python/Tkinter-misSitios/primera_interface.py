from tkinter import *
raiz=Tk()  #con esto se crea la raíz
raiz.title("Ventana de prueba")
raiz.resizable (1,1)  #width ancho, heght = alto ...  no se puede agrandar el borde de la ventana es un boolean
#raiz.geometry("650x350") #ancho y alto, la raíz se acomoda al tamaño del frame ( por eso la desactive)
raiz.config(bg="SteelBlue1")

raiz.iconbitmap('/Users/Jose Láscar/Desktop/GUI/gato.ico')

miFrame=Frame()
miFrame.pack(side="left") #opción donde dejo anclado el frame / punto cardinal dnd lo ubico
miFrame.pack(fill="y")

miFrame.config(bg="green")
miFrame.config(width="650", height="350")

miLabel=Label(miFrame, text="Holaaa")
miLabel.place(x=100, y=200)
miLabel.pack()

miFrame.config(bd=5) #borde para el frame
miFrame.config(relief="groove") #groove,sunken
miFrame.config(cursor="hand2") #pirate



raiz.mainloop() #este es el loop donde la ventana se mantiene funcionando



#todas las configuraciones puedes ser usadas en la RAIZ y en el FRAME


