from django.shortcuts import render

# Create your views here.


def home(request, plantilla="home.html"):
    return render(request, plantilla)

def about(request, plantilla="about.html"):
    return render(request, plantilla)

def contact(request, plantilla="contact.html"):
    return render(request, plantilla)

def bodega(request, plantilla="bodega.html"):
    return render(request, plantilla)

def cliente(request, plantilla="cliente.html"):
    return render(request, plantilla)

def factura(request, plantilla="factura.html"):
    return render(request, plantilla)

def mecanico(request, plantilla="mecanico.html"):
    return render(request, plantilla)