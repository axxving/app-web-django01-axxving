from django.shortcuts import render, HttpResponse

# Create your views here.

def hola_work(request):
    return HttpResponse("""
                        <h1>Hola trabajo desde Django</h1>
                        <p>Esto es un parrafo</p>
                        """)

def index(request):
    return HttpResponse("""
                        <h1>Inicio</h1>
                        """)

def page_pruebas(request):
    return HttpResponse("""
                        <h1>Pagina de pruebas</h1>
                        """)

# MVC - Modelo Vista Controlador -> Acciones (Metodos)

# MVT - Modelo Vista Template -> Acciones (Metodos)