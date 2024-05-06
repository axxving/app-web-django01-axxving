from django.shortcuts import render, HttpResponse

# Create your views here.
# MVC = Modelo vista controlador -> Acciones (metodos)
# MVT = Modelo vista template -> (metodos)

def hola_mundo (request):
    return HttpResponse("<h1>Hello work with Django</h1>")