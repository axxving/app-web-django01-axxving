from django.shortcuts import render, HttpResponse

#
layout = """
<h1>Sitio Web</h1>
</hr>
<ul>
    <a href="/">Inicio</a>
    <a href="/hola-work">Hola Trabajo</a>
    <a href="/page">Pagina de pruebas</a>
</ul>
</hr>
"""


# Create your views here.

def hola_work(request):
    return HttpResponse(layout + """
                        <h1>Hola trabajo desde Django</h1>
                        <p>Esto es un parrafo</p>
                        """)

def page_pruebas(request):
    return HttpResponse(layout + """
                        <h1>Pagina de pruebas</h1>
                        """)

def index(request):
    html = """ 
        <h1>Usando una variable</h1> 
        <p>Anios hasta el 2050:</p>
        <ul>
    """

    year = 2021
    while year <= 2050:

        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year += 1

    html += "</ul>"

    return HttpResponse(layout+html)

# MVC - Modelo Vista Controlador -> Acciones (Metodos)

# MVT - Modelo Vista Template -> Acciones (Metodos)