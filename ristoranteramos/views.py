from django.shortcuts import render
from ristoranteramos.models import *

# Create your views here.

def go_inicio(request):
def go_home(request):
    return render(request, 'home.html')

def go_contacto(request):
    return render(request, 'contacto.html')