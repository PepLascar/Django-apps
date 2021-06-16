from django import forms #formularios
from django.core import validators #validadores
from django.contrib.auth.forms import UserCreationForm # formularios por defecto
from django.contrib.auth.models import User  # modelo de Usuario para crear el formulario


class RegisterForm(UserCreationForm): # formulario creado en base a una clase llamada RegisterForm, hereda de UserCreationForm
    class Meta:
        model  = User  #modelo en el cual se va a basar el formulario
        fields = [
            'username', 
            'email', 
            'first_name',  #campos que tiene el modelo para representar visualmente en el formulario
            'last_name', 
            'password1', 
            'password2']    

      
class FormArticle(forms.Form): #vamos a heradar de form para obtener esos campos
    
    title = forms.CharField(
        label= 'Título', #etiqueta física del campo del formulario
        max_length=15,
        required=True, #campo requerido True
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingresa el título (máximo 8 caracteres)',
                'class': 'titulo_form_article'
            }
        ),

        validators=[
            validators.MinLengthValidator(3, 'El título es muy corto'),
            validators.RegexValidator('^[A-Za-z0-9]*$', 'El título está mal formado', 'invalid_title') #validar meter solo letras, expresion regular
        ]

    )

    content = forms.CharField(
        label = 'Contenido',
        widget = forms.Textarea,  #Los widget son campos visuales.
        required=False,
        validators= [
            validators.MaxLengthValidator(100, 'Has exedido el largo del texto!')
        ]
    )
    content.widget.attrs.update({
                'placeholder': 'Ingresa el contenido',
                'class': 'contenido_form_article',   #Crearle una class y un id al html
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


