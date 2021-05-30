from tkinter import *
raiz=Tk()  #con esto se crea la raíz
raiz.title("Ventana de prueba")
raiz.resizable (1,1)  #width ancho, heght = alto ...  no se puede agrandar el borde de la ventana es un boolean
raiz.geometry("650x350") #ancho y alto
raiz.config(bg="blue")
raiz.mainloop() #este es el loop donde la ventana se mantiene funcionando


