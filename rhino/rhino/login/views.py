from django.shortcuts import render, redirect
from .forms import FormularioRegistro
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def registro(req):    
    if req.user.is_authenticated:
        return redirect('/home')

    else:        
        formulario = FormularioRegistro()

        if req.method == 'POST':
            formulario = FormularioRegistro(req.POST)

            if formulario.is_valid():
                formulario.save()
                messages.success(req,'¡Te has registrado correctamente! Ahora te puedes loguear.')
                return redirect(to='login')                                         
        
        return render(req, 'registro.html', {
            'formulario': formulario
        })

def loguear(req):
    if req.user.is_authenticated: 
        return redirect(to='home')   

    elif req.method == 'POST':
            username = req.POST.get('username')
            password = req.POST.get('password')
            user = authenticate(req, username=username, password=password)

            if user is not None:                          
                login(req, user)
                messages.success(req,'Login correcto!')
                return redirect(to='home')   
            else:
                messages.warning(req, 'No te has identificado correctamente. Vuelve a intentarlo.')
    return render (req, 'login.html')

@login_required
def desconectarse(req):
    logout(req)
    messages.success(req,'Hasta pronto!')
    return redirect (to='login')
    