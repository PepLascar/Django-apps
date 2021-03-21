from tkinter import *

ventana = Tk()

ventana.geometry("500x500")

#keyword argument
texto = Label(ventana, text = "Bienvenido al programa")
texto.config(
            fg='white',
            bg='#000000',
            padx=20, # margen en X
            pady=20,
            font=('Calibri', 30)

)
texto.pack()    



texto = Label(ventana, text = "Soy Jose Lascar")

ventana.mainloop()