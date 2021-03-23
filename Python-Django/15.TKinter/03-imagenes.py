#Pillow cargar imágenes dentro del programa

from tkinter import *
from PIL import Image, ImageTk
ventana = Tk()
ventana.geometry('700x500')

Label(ventana, text='Hola estamos en la ventana').pack(anchor=W)

imagen = Image.open('./15.TKinter/img/android-17.jpg')  #cargamos la imagen
render = ImageTk.PhotoImage(imagen) #le pasamos al objeto phoimage para que suba la foto

Label(ventana, image=render).pack(anchor=E)  #usamos ventana y la imagen para que cargue el pack 

ventana.mainloop()