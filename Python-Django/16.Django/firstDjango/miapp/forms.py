#creación de formularios con POO Python
# DOCUMENTACIÓN FORMS fields django
#Aquí puedo darle formato y validaciones al formulario a nivel de html

from django import forms
from django.core import validators  #improtte para validar diferentes tipos de datos

class FormArticle(forms.Form): #vamos a heradar de form para obtener esos campos
    
    title = forms.CharField(
        label= 'Título', #etiqueta física del campo del formulario
        max_length=30,
        required=True, #campo requerido True
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingresa el título (máximo 30 caracteres)',
                'class': 'titulo_form_article'
            }
        )
    )

    content = forms.CharField(
        label = 'Contenido',
        widget = forms.Textarea
    )
    content.widget.attrs.update({
                'placeholder': 'Ingresa el contenido',
                'class': 'contenido_form_article',
                'id': 'contenido_form'
        })

    public_options = [
        (1,'Si'),
        (0,'No')
    ]

    public = forms.TypedChoiceField(
        label = "¿Publicado?",
        choices = public_options    
    )


    """,
        validators=[
            validators.MinLengthValidator(4, 'El título es muy corto')
            validators.RegexValidator('^[A-Za-z0-9]*$', 'El título está mal formado', 'invalid_title') #validar meter solo letras, expresion regular
        ]"""
