from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404

from ristoranteramos.forms import *
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroFormulario, LoginFormulario
from ristoranteramos.models import *

# Create your views here.
def es_admin(user):
    if not user.is_authenticated or not user.rol == 'administrador':
        raise PermissionDenied
    return True

def go_home(request):
    return render(request, 'home.html')

def go_contacto(request):
    return render(request, 'contacto.html')

def go_login(request):
    return render(request, 'log-in.html')

@user_passes_test(es_admin)
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
        # Registro
        if 'email' in request.POST and 'password' in request.POST:
            registro_form = RegistroFormulario(request.POST)
            if registro_form.is_valid():
                usuario = registro_form.save(commit=False)
                usuario.set_password(registro_form.cleaned_data['password'])

                # Si no se envió rol, se pone por defecto "cliente"
                if not usuario.rol:
                    usuario.rol = 'cliente'

                usuario.save()
                return redirect('log_in_page')
        else:
            # Login
            login_form = LoginFormulario(request, data=request.POST)
            if login_form.is_valid():
                email = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                usuario = authenticate(request, username=email, password=password)
                if usuario is not None:
                    login(request, usuario)
                    # Verificamos si es administrador
                    if usuario.rol == 'administrador':
                        return redirect('empleados')  # ← Aquí redirige a verEmpleados.html
                    else:
                        return redirect('inicio')  # ← Otros roles van a 'inicio'

    return render(request, 'log-in.html', {
        'registro_form': registro_form,
        'login_form': login_form
    })

def logout_usuario(request):
    logout(request)
    return redirect('log_in_page')

@login_required
def actualizar_foto(request):
    if request.method == 'POST' and 'foto' in request.FILES:
        usuario = request.user
        usuario.foto = request.FILES['foto']
        usuario.save()
        return redirect('inicio')  # Puedes redirigir donde quieras
    return redirect('inicio')



@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = FormularioEditarPerfil(request.POST, instance=request.user)
        if form.is_valid():
            form.save()  # Guarda los cambios
            return redirect('home')  # Redirige a la página de inicio (home) para ver los cambios
    else:
        form = FormularioEditarPerfil(instance=request.user)

    return render(request, 'home.html', {'form': form})