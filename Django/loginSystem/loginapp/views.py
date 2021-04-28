from django.shortcuts import render, redirect
from .models import User
import mysql.connector
from operator import itemgetter
from django.contrib import messages

# select * from loginapp_user;
# https://codeforcoders.com/projects/django/login-system-abstract-user

def welcome(req):
    return render(req,'welcome.html')

def login(req):  # CREAR CURSOR 3 y obtener USUARIO desde la database
    con = mysql.connector.connect(host='localhost', user='root', passwd='1234', database="django")
    cursor=con.cursor()

    con2 = mysql.connector.connect(host='localhost', user='root', passwd='1234', database="django")
    cursor2=con2.cursor()

    con3 = mysql.connector.connect(host='localhost', user='root', passwd='1234', database="django")
    cursor3=con3.cursor()

    query1 = "SELECT email from loginapp_user"
    query2 = "SELECT password from loginapp_user"
    query3 = "SELECT fname from loginapp_user"
    cursor.execute(query1)
    cursor2.execute(query2)
    cursor3.execute(query3)

    email  = []
    passwd = []
    nombre = []
        
    for i in cursor:
        email.append(i)
    for j in cursor2:
        passwd.append(j)
    for n in cursor3:
        nombre.append(n)
    res  = list(map(itemgetter(0), email))
    res2 = list(map(itemgetter(0), passwd))
    res3 = list(map(itemgetter(0), nombre))

    if req.method=="POST":

        email = req.POST['email']
        password = req.POST['password']
        k=len(res)
        i=1

        inxMail = email.index(email)        
        nom = nombre.append(res3)

        while i <k:
            if res[i]==email and res2[i]==password:
                return render(req,'welcome.html',{'email':email})
            i+=1
            print(f'Nombre de usuario {nom}')
            print(f"Correo logueado {email}")
        else:
            messages.info(req,"Check username or password")
            return redirect('login')
    return render(req,'login.html')

"""print(res)
    print("\n")
    print(passwd)
    print(email)"""


def register(req):
    if req.method=="POST":
        user = User()

        user.fname = req.POST['fname']
        user.lname = req.POST['lname']
        user.email = req.POST['email']
        user.password = req.POST['password']
        user.repassword = req.POST['repassword']

        if user.password != user.repassword:
            return redirect('register.html')

        elif user.fname == "" or user.password == "":
            messages.info(req, 'some fields are empty')
            return redirect('register.html')

        else:
            user.save()            

    return render(req,'register.html')



