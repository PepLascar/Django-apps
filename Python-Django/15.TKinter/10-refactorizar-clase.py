from tkinter import *
from tkinter import messagebox



class Calculadora:

    # Funciones asociadas al programa.
    # Para hacer una clase difinir parámetro self

    #función para asignarle valor a las propiedades. CONSTRUCTOR
    def __init__(self, alertas):
        self.num1 = StringVar()
        self.num2 = StringVar()
        self.resultado = StringVar()
        self.alertas = alertas


    def comprobarFloat(self, numero): #def para comprobar y usar en otras def. No activada.
        try:
            resu = float(numero)
        except:
            resu = 0
            messagebox.showerror("Error", "Número no válido.")
        return resu

    def sumar(self):
        try:
            self.resultado.set(float(self.num1.get()) + float(self.num2.get( ) ))
            self.mostrarResultado()
        except:
            self.alertas.showerror("Error", "Introducir sólo números.") #método showerror lleva 3 parámetros.

    def restar(self):
        self.resultado.set(float(self.num1.get()) - float(self.num2.get()))
        self.mostrarResultado()

    def multi(self):
        self.resultado.set(float(self.num1.get()) * float(self.num2.get()))
        self.mostrarResultado()

    def dividir(self):
        self.resultado.set(float(self.num1.get()) / float(self.num2.get()))
        self.mostrarResultado()

    def mostrarResultado(self):
        self.alertas.showinfo("Resultado", f"El resultado es {self.resultado.get()}")


#-----------------------------------
ventana = Tk()
ventana.title("Calculadora Python | Tkinter")
ventana.geometry("400x400")
ventana.config(bd=25)

# AttributeError: 'NoneType' object has no attribute '_root' - pasarle el objeto messegebox ya que está trabajando con ellos.
calculadora = Calculadora(messagebox)  #Creo un objeto calculadora para acceder a sus propiedades.

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
Entry(marco, textvariable=calculadora.num1, justify="center").pack()

#Segundo imput
Label(marco, text="Segundo número: ").pack()
Entry(marco, textvariable=calculadora.num2, justify="center").pack()

Label(marco, text="").pack()
                                # ejecuto def por calculadora.sumar
Button(marco, text="SUMAR",   command=calculadora.sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="RESTAR",  command=calculadora.restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="MULTI",   command=calculadora.multi).pack(side="left", fill=X, expand=YES)
Button(marco, text="DIVIDIR", command=calculadora.dividir).pack(side="left", fill=X, expand=YES)


ventana.mainloop()