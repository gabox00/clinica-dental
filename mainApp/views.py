from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, User
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def index(request):

    return render(request, 'mainApp/index.html', {'title': 'Inicio'})

def about(request):

    return render(request, 'mainApp/about.html', {'title': 'Sobre mi'})

def registerUser(request):

    if request.user.is_authenticated:
        return redirect('index')
    else:
        register_form = RegisterForm()

        if request.method == "POST":
            register_form = RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()
                messages.success(request,"Te has registrado correctamente")
                return redirect('index')

        return render(request, 'users/register.html', {
            'title': 'Registro',
            'register_form': register_form
        })

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                messages.success(request,f"Bienvenido {user.first_name} {user.last_name}")
                return redirect('index')
            else:
                messages.warning(request,"No te has identificado correctamente")

        return render(request, "users/login.html", {
            'title': 'Iniciar Sesion'
        })

def logoutUser(request):
    logout(request)
    return redirect('login')