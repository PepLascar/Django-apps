from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Calculadora Python | Tkinter")
ventana.geometry("400x400")
ventana.config(bd=25)

#marco para contener los elementos
def comprobarFloat(numero): #def para comprobar y usar en otras def. No activada.
    try:
        resu = float(numero)
    except:
        resu = 0
        messagebox.showerror("Error", "Número no válido.")
    return resu

def sumar():
    try:
        resultado.set(float(num1.get()) + float(num2.get( ) ))
        mostrarResultado()
    except:
        messagebox.showerror("Error", "Introducir sólo números.") #método showerror lleva 3 parámetros.

def restar():
    resultado.set(float(num1.get()) - float(num2.get()))
    mostrarResultado()

def multi():
    resultado.set(float(num1.get()) * float(num2.get()))
    mostrarResultado()

def dividir():
    resultado.set(float(num1.get()) / float(num2.get()))
    mostrarResultado()

def mostrarResultado():
    messagebox.showinfo("Resultado", f"El resultado es {resultado.get()}")

num1 = StringVar()
num2 = StringVar()
resultado = StringVar()

marco = Frame(ventana, width=250, height=250)
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False) #Para que no se desforme el marco


#Label para primer input
Label(marco, text="Primer número: ").pack()
Entry(marco, textvariable=num1, justify="center").pack()

#Segundo imput
Label(marco, text="Segundo número: ").pack()
Entry(marco, textvariable=num2, justify="center").pack()

Label(marco, text="").pack()

Button(marco, text="SUMAR", command=sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="RESTAR", command=restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="MULTI", command=multi).pack(side="left", fill=X, expand=YES)
Button(marco, text="DIVIDIR", command=dividir).pack(side="left", fill=X, expand=YES)


ventana.mainloop()