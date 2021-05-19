from django.shortcuts import render
from blog.models import Category, Article #Importando elementos del modelo para mostrar

# Create your views here.

def list(req):

    articles = Article.objects.all() # Traer todos los objetos

    return render(req, 'articles/list.html', {
        'title': 'Artículos',
        'articles': articles
    })
