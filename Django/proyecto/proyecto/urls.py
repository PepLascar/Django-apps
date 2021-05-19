from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include  #con esto cargo las rutas del admin con path
from django.conf import settings


#recordar que tenemos templates con url amigables en el django admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')), #URLS app main
    path('', include('pages.urls')),   #URLS app pages
    path('', include('blog.urls')),    #URLS app blog
]

# Ruta imagenes para poder visualizarlas en django
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)  #en el segundo parametro indicar el path de carpeta media

#Se pueden tener ficheros de URL en cada APP
# Cada app en si debería tener su propia configuración