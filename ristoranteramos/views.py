from django.shortcuts import render, redirect

from ristoranteramos.forms import FormularioEmpleado
from ristoranteramos.models import *

# Create your views here.
def go_home(request):
    return render(request, 'home.html')

def go_contacto(request):
    return render(request, 'contacto.html')

def go_administrador(request):
    return render(request, 'anadirEmpleado.html')

def new_empleado(request):

    # if request.method == 'POST':
    #     Id = request.POSTget('Id', '')
    #     Nombre = request.POST.get('Nombre', '')
    #     Rol = request.POST.get('Rol', '')
    #
    #     nuevo_empleado = Empleado()
    #     nuevo_empleado.Id = Id
    #     nuevo_empleado.Nombre = Nombre
    #     nuevo_empleado.Rol = Rol
    #
    #     # nuevo_empleado.save()
    #     "Insert into empleados (Id,Nombre,Rol) values (%s,%s,%s)"

    if request.method == 'POST':
        form = FormularioEmpleado(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
            form = FormularioEmpleado()

    return render(request, 'anadirEmpleado.html',{'form':form})