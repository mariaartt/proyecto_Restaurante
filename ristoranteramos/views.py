from django.shortcuts import render, redirect

from ristoranteramos.forms import *
from ristoranteramos.models import *

# Create your views here.
def go_home(request):
    return render(request, 'home.html')

def go_contacto(request):
    return render(request, 'contacto.html')

def go_login(request):
    return render(request, 'log-in.html')

def go_empleados(request):
    return render(request, 'verEmpleados.html')

def go_articulos(request):
    return render(request, 'verArticulo.html')

def new_empleado(request):
    if request.method == 'POST':
        form = FormularioUsuario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleados')
    else:
            form = FormularioUsuario()

    return render(request, 'anadirEmpleado.html',{'form':form})

def new_articulo(request):
    if request.method == 'POST':
        form = FormularioArticulo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articulos')
    else:
            form = FormularioArticulo()

    return render(request, 'anadirArticulo.html',{'form':form})