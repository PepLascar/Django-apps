#Tkinter: Modulo para crear interfaces gráficas de usuario.

import os
os.system('cls')
os.path



from tkinter import *

class Programa:
    def __init__(self): #Constructor, una clase para tener un constructor para crear ventanas.
        self.title = "Trabajando con Tkinter"
        self.icon  =  './15.TKinter/gato.ico'
        self.size = "750x450"
        self.resisable = False
    
    def cargar(self): # Método para cargar el programa

        # Crear ventana raiz, objeto Tk() crea la ventana
        ventana = Tk()
        self.ventana = ventana

        # Crear rutas
        ruta_icono = os.path.abspath(self.icon)
        # Comprobar si existe un archivo - Si esto no se cumple
        if os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon)  #Aquí podría poner la ruta completa.

        # Mostrar texto en la ventana
        texto = Label(ventana, text = ruta_icono)
        texto.pack()

        # TÍTULO VENTANA
        ventana.title(self.title)

        # Tamaño ventana
        ventana.geometry(self.size)   

        # Bloquear redimensionar
        if self.resisable:
            ventana.resizable(1,1)        
        else:
            ventana.resizable(0,0)

        # Ícono ventana
        #ventana.iconbitmap("./15.TKinter/gato.ico") 
        ventana.iconbitmap(ruta_icono)

        # Arrancar y mostrar la ventana hasta que se cierre
        # ventana.mainloop()

    def agregarLabel(self, dato):
        texto = Label(self.ventana,text=dato)
        texto.pack()
    
    def mostrar(self):  #MÉTODO PARA ARRANCAR EL MAIN LOOP 
        self.ventana.mainloop()



    #Instanciar programa a través de las clases.
programa = Programa()
programa.cargar()
programa.agregarLabel('Agregarndo cosas')  #No se carga por que el main loop ya se ha ejecutado.
programa.agregarLabel('Agregarndo cosas') 
programa.mostrar()