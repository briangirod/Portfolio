from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from portfolio.models import Poster

class UserEditForm(UserCreationForm):
    
    first_name=forms.CharField(label="Nombre")
    last_name=forms.CharField(label="Apellido")
    email= forms.EmailField(label="Modificar")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la Contraseña", widget=forms.PasswordInput)
    description=forms.CharField(label='Agregar Descripción')
    

    class Meta:
        model = User
        fields= ['first_name','last_name', 'email', 'password1', 'password2', 'description']
        help_text= {k:"" for k in fields}
         
class PostForm(forms.ModelForm):
    content= forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placeholder':'¿Qué esta pasando?'}))
    class Meta:
        model= Poster
        fields= ['content']

class CreateUserForm(UserCreationForm):
    email= forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']