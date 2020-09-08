from django.shortcuts import render, HttpResponse, redirect, get_object_or_404

# Create your views here.
from .forms import clienteForm, Cliente
def cliente(request, plantilla="cliente.html"):
    clientes = Cliente.objects.all()
    data = {
        'cliente':clientes
    }
    return render(request, plantilla, data)

##   pagina de crear o insertar INSERT
def crearcliente(request, plantilla="crearcliente.html"):

    if request.method == "POST":
        form = clienteForm((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect('cliente')
    else:
        form = clienteForm

    return render(request, plantilla, {'form': form})

## pagina de modificar o update
def modificarcliente(request, pk, plantilla="modificarcliente.html"):

    if request.method == "POST":
        cliente = get_object_or_404(Cliente, pk=pk)
        form = clienteForm(request.POST or None, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente')
    else:
        cliente = get_object_or_404(Cliente, pk=pk)
        form = clienteForm(request.POST or None, instance=cliente)

    return render(request, plantilla, {'form': form})

## pagina de eliminar o delete
def eliminarcliente(request, pk, plantilla="eliminarcliente.html"):

    if request.method == "POST":
        form = clienteForm((request.POST or None))
        cliente = get_object_or_404(Cliente, pk=pk)
        if form.is_valid():
            cliente.delete()
            return redirect('cliente')
    else:
        cliente = get_object_or_404(Cliente, pk=pk)
        form = clienteForm(request.POST or None, instance=cliente)

    return render(request, plantilla, {'form': form})