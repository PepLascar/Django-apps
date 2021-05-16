from django.contrib import admin
from django.urls import path, include  #con esto cargo las rutas del admin con path


#recordar que tenemos templates con url amigables en el django admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')), #URLS app main
    path('', include('pages.urls')),   #URLS app pages
    path('', include('blog.urls')),    #URLS app blog
]

#Se pueden tener ficheros de URL en cada APP
# Cada app en si debería tener su propia configuración