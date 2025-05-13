from django.shortcuts import render, redirect, get_object_or_404

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
    empleados = Usuario.objects.all()
    return render(request, 'verEmpleados.html', {"empleados": empleados})

def new_empleado(request, id):
    empleado = get_object_or_404(Usuario, id=id)

    if request.method == 'POST':
        form = FormularioUsuario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleados')
    else:
            form = FormularioUsuario()

    return render(request, 'anadirEmpleado.html',{'form':form}, {'empleado':empleado})

def editar_empleado(request, id):
    if id != 0:
        usuario = get_object_or_404(Usuario, id=id)
    else:
        usuario = None

    if request.method == 'POST':
        form = FormularioUsuario(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('empleados')
        else:
            return render(request, 'anadirEmpleado.html',{'form':form})
    else:
        form = FormularioUsuario(instance=usuario)

    return render(request, 'anadirEmpleado.html',{'form':form})

def eliminar_empleado(request, id):
    empleado_eliminar = Usuario.objects.filter(id=id)

    if len(empleado_eliminar) != 0:
        empleado_eliminar[0].delete()
        return redirect('empleados')

def go_articulos(request):
    articulos = ArticuloCarta.objects.all()
    return render(request, 'verArticulo.html', {"articulos": articulos})

def new_articulo(request, id):
    articulo = get_object_or_404(ArticuloCarta, id=id)

    if request.method == 'POST':
        form = FormularioArticulo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articulos')
    else:
            form = FormularioArticulo()

    return render(request, 'anadirArticulo.html',{'form':form}, {'articulo':articulo})

def editar_articulo(request, id):
    if id != 0:
        articulo = get_object_or_404(ArticuloCarta, id=id)
    else:
        articulo = None

    if request.method == 'POST':
        form = FormularioArticulo(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('articulos')
        else:
            return render(request, 'anadirArticulo.html',{'form':form})
    else:
        form = FormularioArticulo(instance=articulo)

    return render(request, 'anadirArticulo.html',{'form':form})

def eliminar_articulo(request, id):
    articulo_eliminar = ArticuloCarta.objects.filter(id=id)

    if len(articulo_eliminar) != 0:
        articulo_eliminar[0].delete()
        return redirect('articulos')

