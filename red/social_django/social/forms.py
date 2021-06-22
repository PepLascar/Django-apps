from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class Formulario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)   #que tipo de tag va a ser en el html
    password2 = forms.CharField(label='Confirma contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']  #queremos que aparezca
        help_texts = {k:"" for k in fields }  #iterar en campos y poner textos cacíos


#Formulario del post
class PostForm(forms.ModelForm):
	content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placeholder': '¿Qué está pasando?'}), required=True) #dandole formato al campo del formulario
                                            #obteniendo campos del contenido
	class Meta:
		model = Post
		fields = ['content']