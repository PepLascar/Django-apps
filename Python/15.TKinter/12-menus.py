from tkinter import *

ventana = Tk()
ventana.geometry("700x400")

mi_menu = Menu(ventana) #variable con un objeto menu, cargado en ventana

ventana.config(menu=mi_menu) #al atributo menu le paso la variable mi_menu  #Con cascade se agregan desplegables

archivo = Menu(mi_menu, tearoff=0)  # var archivo vinculada al objeto Menu
archivo.add_command(label= "Nuevo ")
archivo.add_command(label= "Abrir")
archivo.add_command(label= "Guardar")
archivo.add_separator()
archivo.add_command(label= "Salir", command=ventana.quit)


mi_menu.add_cascade(label= "Opciones", menu=archivo)
mi_menu.add_command(label= "Editar")
mi_menu.add_command(label= "Revisar")

ventana.mainloop()


