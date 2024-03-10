from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import ContactoForm
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def home(request):
    return render(request, 'home.html',)


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})
    
def cerrarsesion(request):
    logout(request)
    return redirect ("index")


@csrf_exempt
def contacto(request):
    data = {"form": ContactoForm()}
    if request.method == "POST":
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario
    return render (request, "index.html", data)


def signin(request):
    return render(request, "signin.html")

def index(request):
    return render(request, "index.html")