from django.shortcuts import render

# Create your views here.

def go_inicio(request):
    return render(request, 'base.html')

def go_contacto(request):
    return render(request, 'contacto.html')
