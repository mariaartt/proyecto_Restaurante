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