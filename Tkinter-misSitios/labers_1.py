from tkinter import * 
root=Tk()
miFrame=Frame(root, width=500, height=400)
miFrame.pack()
raiz.iconbitmap('/Users/Jose Láscar/Desktop/GUI/gato.ico')

miImagen=PhotoImage(file="logogif.gif")

Label(miFrame, image=miImagen).place(x=100, y=100)




root.mainloop()



