from tkinter import *
from tkinter import ttk

# Configuración ventana
ventana = Tk()
#ventana.geometry("500x500")
ventana.minsize(400,400)
ventana.title("Pyton Tkinter | Aplicación escritorio")
ventana.resizable(0,0)


# 2.Pantallas (cada una de ellas es una def) 
def home():
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial",20),
        padx=170,
        pady=20
    )
    home_label.grid(row=0, column=0)
    product_box.grid(row=2)
    
    """#Listar productos
    for i in productos:
        if len(i) == 3:   #mostrar los campos que tengan 3 elementos
            i.append("Añadido")
            Label(product_box, text=i[0]).grid()
            Label(product_box, text=i[1]).grid()
            Label(product_box, text=i[2]).grid()
            Label(product_box, text="---------").grid()"""

    for i in productos:
        if len(i) == 3:
            i.append("Añadido")
            product_box.insert('',0, text=i[0], values = (i[1]))

    #Ocultar otras pantalla
    add_label.grid_remove()
    nuevo_frame.grid_remove()
    info_label.grid_remove()
    datos_label.grid_remove()
    

    """add_name_label.grid_remove()
    add_name_entry.grid_remove()
    add_price_label.grid_remove()
    add_price_entry.grid_remove()
    add_desc_label.grid_remove()
    add_desc_entry.grid_remove()
    add_desc_entry.grid_remove()"""

def add():
    add_label.config(
        fg="white",
        bg="black",
        font=("Consolas",20),
        padx=170,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=8)

    #Campos del formulario en ADD
    nuevo_frame.grid(row=1)
    add_name_label.grid(row=1,column=0, padx=5, pady=5, sticky=W)
    add_name_entry.grid(row=1,column=1, padx=5, pady=5, sticky=W)

    add_price_label.grid(row=2,column=0, padx=5, pady=5, sticky=W)
    add_price_entry.grid(row=2,column=1, padx=5, pady=5, sticky=W)

    add_desc_label.grid(row=3,column=0, padx=5, pady=5, sticky=W)
    add_desc_entry.grid(row=3,column=1, padx=5, pady=5, sticky=W)
    add_desc_entry.config(
        width=30,
        height=5,
        font=("Consolas", 12),
        padx=15,
        pady=15
    )

    add_separador.grid(row=4, column=0)

    boton.grid(row=5, column=1, sticky=NE)
    boton.config(
        padx=15,
        pady=5,
        bg="green",
        fg="white"
    )
    home_label.grid_remove()  
    info_label.grid_remove()
    datos_label.grid_remove()  
    product_box.grid_remove()

def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Consolas",20),
        padx=170,
        pady=20
    )
    info_label.grid(row=0, column=0)
    datos_label.grid(row=1,column=0)

    add_label.grid_remove()
    home_label.grid_remove()
    nuevo_frame.grid_remove()
    product_box.grid_remove()
    """add_name_label.grid_remove()
    add_name_entry.grid_remove()
    add_price_label.grid_remove()
    add_price_entry.grid_remove()
    add_desc_label.grid_remove()
    add_desc_entry.grid_remove()
    add_desc_entry.grid_remove()"""

def add_producto():  #Crear una lista para obtener los datos de las otras variables.
    productos.append([
        name_data.get(),
        price_data.get(),
        add_desc_entry.get("1.0","end-1c") 
        ])
    name_data.set("")
    price_data.set("")
    add_desc_entry.delete("1.0",END )

    home()  #usar este método me redirige a Home
    print(productos) #Mostrar la lista produtos


# VARIABLES
productos  = []
name_data  = StringVar()
price_data = StringVar()
desc_data  = StringVar()


# Definir objetos de las pantallas - para tener acceso a las variables dentro de las funciones. inicio, añadir, información, etc.
home_label  = Label(ventana, text="Inicio")
#product_box = Frame(ventana, width=250)

# -Treeview-
#Label(product_box).grid(row=0)
Label(ventana).grid(row=1)
product_box = ttk.Treeview(height=12, columns=2)
product_box.grid(row=1, column=0, columnspan=2)
product_box.heading("#0", text='Producto', anchor=W) #creando columnas
product_box.heading("#1", text='Precio', anchor=W) #creando columnas



add_label   = Label(ventana, text="Añadir producto")
info_label  = Label(ventana, text="Información")
datos_label = Label(ventana, text="Desarrollado por Lco")


# 4. Campos del formulario para ADD. Aquí se crean labels, entrys, button, separator para luego usarlos.
# 5. Crear frames para no ocultar 1 a 1 los elementos del programa. Antes los teniamos en "ventana" ahora en nuevo_frame
nuevo_frame = Frame(ventana)

add_name_label = Label(nuevo_frame , text="Nombre: ")
add_name_entry = Entry(nuevo_frame , textvariable=name_data)

add_price_label = Label(nuevo_frame , text="Precio: ")
add_price_entry = Entry(nuevo_frame , textvariable=price_data)

add_desc_label = Label(nuevo_frame , text="Descripción: ")
add_desc_entry = Text(nuevo_frame )

add_separador = Label(nuevo_frame )
boton = Button(nuevo_frame , text="Guardar", command=add_producto) #command es para ejecutar funciones

# 3. Cargar pantalla de inicio
home()

# 1. Head Menu
menu_superior = Menu(ventana) #Obj menu creado en var ventana
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Información", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)
#Cargar el Menu
ventana.config(menu=menu_superior) #al parámetro menu se le entrega var menu_sup


ventana.mainloop()