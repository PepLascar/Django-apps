from django.contrib import admin
from django.urls import path, include  #con esto cargo las rutas del admin con path


#recordar que tenemos templates con url amigables en el django admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('', include('pages.urls')),
]

#Se pueden tener ficheros de URL en cada APP
# Cada app en si debería tener su propia configuración