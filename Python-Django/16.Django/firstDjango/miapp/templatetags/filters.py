#PACKAGE

from django import template

register = template.Library()

@register.filter(name='saludo')    #decorador: funcionalidad previa a una clase o función
def saludo(valor):
    largo = ''
    if len(valor) >= 8:
        largo = '<p>Tu nombre es muy largo</p>'

    return f"<h1 style='background:green;color:white;'>Bienvenido, {valor} </h1>" + largo