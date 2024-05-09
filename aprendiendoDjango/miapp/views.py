from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

# Hola Work
def hola_work(request):
    return render(request, 'work.html')

# Pagina de pruebas
def pagina(request):
    return render(request, 'pagina.html')

# Index
def index(request):
    return render(request, 'index.html')

# Contacto
def contacto(request):
    return render(request, 'contacto.html')

# MVC - Modelo Vista Controlador -> Acciones (Metodos)

# MVT - Modelo Vista Template -> Acciones (Metodos)