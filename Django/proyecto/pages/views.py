from django.shortcuts import render
from .models import Page #importo modelo de page
# Crear vista que saque 1 página de la BD

def page(req, slug):

    #obteniendo datos reales
    page = Page.objects.get(slug=slug) #comparo que el slgu sea igual al de la url

    return render(req, "pages/page.html", { #paso la template
        "page": page  #obteniendo un objeto page
    })  
