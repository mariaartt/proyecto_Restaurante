from django.shortcuts import render
from ristoranteramos.models import *

# Create your views here.
def go_home(request):
    return render(request, 'home.html')

def go_contacto(request):
    return render(request, 'contacto.html')

def go_carta(request):
    return render(request, 'carta.html')

def go_login(request):
    return render(request, 'log-in.html')

def go_reporte_ventas(request):
    return render(request, 'reporteVentas.html')