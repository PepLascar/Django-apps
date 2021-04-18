import os
os.system ("cls")
import webbrowser
from tkinter import *

root = Tk()
root.title("JL")
root.resizable (0,0)
root.config(bg="SteelBlue1")
root.iconbitmap('/Users/Jose Láscar/Desktop/GUI/gato.ico')
root.geometry('200x480')

def santander():
    webbrowser.open('www.santander.cl')
def google():
    webbrowser.open('www.google.cl')
def anime():
    webbrowser.open('www.anime-planet.com')
def duoc():
    webbrowser.open('https://ssoprd.duoc.cl/auth/realms/WEB_APPS_PRD/protocol/openid-connect/auth?client_id=411f013c&nonce=478fd98899982560d93588527f22895e&redirect_uri=https%3A%2F%2Fexperienciavivo.duoc.cl%2Fauth%2Fopenidc%2Fcallback&response_type=code&scope=openid&state=40c84005a94b35133dddd082aee3aa6f#')
def ava():
    webbrowser.open('https://campusvirtual.duoc.cl/webapps/login/')
def youtube():
    webbrowser.open('www.youtube.com')
def instagram():
    webbrowser.open('www.instagram.com')

#Botones
santander = Button(root, text='Ir a Banco', bg="slate blue", cursor="hand2", command=santander).pack(pady=20)
google    = Button(root, text='Google', bg="slate blue", cursor="hand2", command=google).pack(pady=20)
anime     = Button(root, text='Ver animé', bg="slate blue", cursor="hand2", command=anime).pack(pady=20)
duoc      = Button(root, text='Ir a Duoc', bg="slate blue", cursor="hand2", command=duoc).pack(pady=20)
ava       = Button(root, text= 'AVA', bg="slate blue", cursor="hand2", command=ava).pack(pady=20)
youtube   = Button(root, text= 'Youtube', bg="slate blue", cursor="hand2", command=youtube).pack(pady=20)
instagram = Button(root, text= 'Instagram', bg="slate blue", cursor="hand2", command=instagram).pack(pady=20)

root.mainloop()

