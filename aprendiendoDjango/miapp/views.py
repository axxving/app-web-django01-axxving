from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

# Hola Work
def hola_work(request):
    return render(request, 'components/work.html')

# Pagina de pruebas
def pagina(request):
    return render(request, 'components/pagina.html')

# Index

def index(request):

    year = 2021
    hasta = range(year, 2050)

    nombre = "Alex"
    lenguajes = [ "JavaScript", "Python", "C" ]

    return render(request, 'components/index.html', {
        'title': 'Inicio',
        'mi_variable': 'Soy un dato que esta en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': hasta
    })

# Contacto
def contacto(request):
    return render(request, 'components/contacto.html')

# MVC - Modelo Vista Controlador -> Acciones (Metodos)

# MVT - Modelo Vista Template -> Acciones (Metodos)