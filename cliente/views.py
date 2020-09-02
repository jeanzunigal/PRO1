from django.shortcuts import render, redirect

# Create your views here.
from .forms import clienteForm, Cliente
def cliente(request, plantilla="usuario.html"):
    clientes = Cliente.objects.all()
    data = {
        'cliente':clientes
    }
    return render(request, plantilla, data)
#pagina de crear o insertar INSERT
def crearcliente(request, plantilla="crearcliente.html"):

    if request.method == "POST":
        form = clienteForm((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect('cliente')
    else:
        form = clienteForm

    return render(request, plantilla, {'form': form})