from blog.models import Category, Article
#función para moatrar las páginas mediante herencia
#Aquí manejo las páginas del django admin como bloque

def get_categories(req): #quiero obtener las categorias

    # consulta para conseguir los ID de las entradas de artículos
    id_cat_en_uso = Article.objects.filter(public=True).values_list('categories', flat=True)  #obtener campo que contiene la ID de la categoría del elemento
    categories = Category.objects.filter(id__in=id_cat_en_uso).values_list('id', 'name') # Procesador de contexto para tenr disponible todas las categorías
                                 # obteniendo las categorias que están en uso

    return {
        'categories': categories,
        'id_cat_en_uso': id_cat_en_uso
    }
