from pages.models import Page

def get_pages(req):
    
    pages = Page.objects.values_list('id', 'title', 'slug') #muestra uno de los elementos que quiero tenr disponible ('title', flat=True)

    #def para saacr las páginas que tenga guardadas en la plantilla
    return {
        'pages': pages
    }
