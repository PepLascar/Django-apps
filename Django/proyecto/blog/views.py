from django.shortcuts import render, get_object_or_404
from blog.models import Category, Article #Importando elementos del modelo para mostrar
from django.core.paginator import Paginator  # PAGINACIÓN
from django.contrib.auth.decorators import login_required  #DECORADOR 296


# Errores, importarlos de django shortcuts
# Create your views here.

@login_required(login_url='login')
def list(req):

    # Traer/obtener todos los objetos (articulos)
    articles = Article.objects.all() 

    # Paginar los articulos
    paginator = Paginator(articles, 2)  # quiero 2 artículos por página

    #obtener número página
    page = req.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(req, 'articles/list.html', {
        'title': 'Artículos',
        'articles': page_articles   #devolver esta variable
    })


def category(req, category_id):
    category = Category.objects.get(id=category_id)
    # category = get_object_or_404(Category, id=category_id)    MOSTRAR CON ERROR 404
    # articles = Article.objects.filter(categories=category)  # obtener artículos por categoría

    return render(req, 'categories/category.html', {
        'category': category
        #'articles': articles
    })


@login_required(login_url='login')
def article(req, article_id):

    article = get_object_or_404(Article, id=article_id)  #si los artículos no están me lanza un 404

    return render(req, 'articles/detail.html', {
        'article': article  #detalle artículos, variables del diccionario
    }) 
