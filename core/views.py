from django.shortcuts import render, redirect

# Create your views here.


def home(request, plantilla="home.html"):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, plantilla)
    # En otro caso redireccionamos al login
    return redirect('login')

def about(request, plantilla="about.html"):
    return render(request, plantilla)

def contact(request, plantilla="contact.html"):
    return render(request, plantilla)

def bodega(request, plantilla="bodega.html"):
    return render(request, plantilla)

def usuario(request, plantilla="usuario.html"):
    return render(request, plantilla)

def factura(request, plantilla="factura.html"):
    return render(request, plantilla)

def mecanico(request, plantilla="mecanico.html"):
    return render(request, plantilla)