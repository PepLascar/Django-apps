from pages.models import Page
#función para moatrar las páginas mediante herencia
#Aquí manejo las páginas del django admin como bloque
def get_pages(req):
    #filtrando para qu emuestre solo pagians visibles
    pages = Page.objects.filter(visible=True).order_by('order').values_list('id', 'title', 'slug') #muestra uno de los elementos que quiero tenr disponible ('title', flat=True)

    #def para saacr las páginas que tenga guardadas en la plantilla
    return {
        'pages': pages
    }
