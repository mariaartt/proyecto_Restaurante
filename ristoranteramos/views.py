from django.shortcuts import render, redirect, get_object_or_404
from ristoranteramos.forms import *
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroFormulario, LoginFormulario
from ristoranteramos.models import *

# Create your views here.
def go_home(request):
    return render(request, 'home.html')

def go_contacto(request):
    return render(request, 'contacto.html')

def go_login(request):
    return render(request, 'log-in.html')

def go_acerca_de(request):
    return render(request, 'acerca_de.html')

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

def log_in(request):
    registro_form = RegistroFormulario()
    login_form = LoginFormulario()

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'register':
            registro_form = RegistroFormulario(request.POST)
            if registro_form.is_valid():
                usuario = registro_form.save(commit=False)
                usuario.set_password(registro_form.cleaned_data['password'])
                usuario.save()
                return redirect('log_in_page')

        elif action == 'login':
            login_form = LoginFormulario(request, data=request.POST)
            if login_form.is_valid():
                email = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                usuario = authenticate(request, username=email, password=password)
                if usuario is not None:
                    login(request, usuario)
                    return redirect('inicio')

    return render(request, 'log-in.html', {
        'registro_form': registro_form,
        'login_form': login_form
    })

def logout_usuario(request):
    logout(request)
    return redirect('log_in_page')

def go_carta(request):
    return render(request, 'carta.html')

def go_login(request):
    return render(request, 'log-in.html')

def go_reporte_ventas(request):
    return render(request, 'reporteVentas.html')

