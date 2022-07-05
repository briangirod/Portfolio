from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comments, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image', 'user',]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba un título hasta 60 caracteres'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Agregue el contenido'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            #'categoria': forms.Select(choices=op, attrs={'class': 'form-control', 'placeholder': 'Seleccione una categoría'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['title', 'body']