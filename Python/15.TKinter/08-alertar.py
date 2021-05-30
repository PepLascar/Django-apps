from tkinter import *
from tkinter import messagebox as MessegeBox   #Módulo para hacer alertas

ventana = Tk()
ventana.geometry("150x90")
ventana.config(bg="green")
ventana.title(" Tkinter | Alertas ")

def sacarAlerta():
    MessegeBox.showinfo("Alerta", "Usando Messge Box")  #showwarning, showerror, etc ...

def salir(nombre):  #Estás seguro que quieres salir?   #Upgrade, mostrar fecha de la alerta
    respuesta = MessegeBox.askquestion("Salir", "¿Quieres continuar?")  #Askquestion, etc ...
    if respuesta == "no":
        MessegeBox.showinfo("Adios!", f"Hasta pronto {nombre} ")
        ventana.destroy()

Button(ventana, text="MOSTRAR ALERTA", command=sacarAlerta).pack(anchor=CENTER)  #command ejecuta alerta

Button(ventana, text="SALIR", command=lambda: salir("Jose")).pack()  #command ejecuta alerta

ventana.mainloop()