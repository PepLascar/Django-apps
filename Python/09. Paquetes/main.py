#Package_Main
#Un paquete tiene una serie de herramientas dentro.
#Se pueden reutilizar estas herramientas en diferentes proyectos
#Cuando se ejecuta un paquete python genera una carpeta de pycaché

#pypi.org   para inslatar paquetes y módulos puedo buscar e instalar módulos y librerías.
#flask y django funcionan como un paquete de funcionalidades por ejemplo.

from mis_packages import pruebas #,herramientas  (se puede hacer así si vienen del mismo pkg)
from mis_packages import herramientas

pruebas.probandoModulo()
herramientas.nombreCompleto("Jose", "Lascar")
