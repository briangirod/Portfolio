from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Project, Avatar
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *


def home(request):
    
    #avatares = Avatar.objects.filter(user=request.user.id)
    #url = {'url': avatares[0].imagen.url}
    projects = Project.objects.all()

    return render(request, 'home.html' , {'projects': projects})#{'url': avatares[0].imagen.url}) #'home.html', {'projects': projects}, 


def about(request):
    return render(request, 'about.html')

def login_request(request):
    return render(request, 'login.html')

def error(request):
    return render(request, 'error404.html')

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data= request.POST)

        if form.is_valid():
            
            usuario= form.cleaned_data.get("username")
            contra= form.cleaned_data.get("password")

            user= authenticate(username=usuario, password=contra)

            if user is not None: ##Agregar POPUP
                login(request, user) 
                avatares = Avatar.objects.filter(user=request.user.id)
                return render(request, "inicio.html")#, {"url": avatares[0].imagen.url}

            else:
                return HttpResponse("Usuario Incorrecto") ##Agregar popup incorrecto
        else:
            return render(request, "fail_user.html")
    
    
    form = AuthenticationForm()

    return render(request, "login.html", {"form":form})

def register(request):

    if request.method == "POST":
        
        form= CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "creado.html") ##PopUp


    else:
        form= CreateUserForm()
    return render(request, "register.html", {"form":form})   




@login_required
def prueba(request): ##Crear post
    pass 

@login_required
def mi_usuario(request):

    usuario=request.user

    if request.method == "POST":
        miFormulario= UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            usuario.first_name=informacion['first_name']
            usuario.last_name=informacion['last_name']
            usuario.email=informacion['email']
            password = informacion['password1']
            usuario.set_password(password)
            usuario.save()

            return render(request, "modifi.html")

    else:
        miFormulario= UserEditForm(initial={'email':usuario.email, 'first_name':usuario.first_name, 'last_name':usuario.last_name})

    return render(request,"mi_usuario.html", {"miFormulario":miFormulario, "usuario":usuario})




def poster(request):
    current_user= get_object_or_404(User, pk=request.user.pk)
    if request.method=='POST':
        form= PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user=current_user
            post.save()
            messages.success(request, 'Post enviado')
            return redirect('/')
    else:
        form =PostForm()
    return render(request, 'poster.html', {'form':form})