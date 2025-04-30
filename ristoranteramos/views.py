from django.shortcuts import render

# Create your views here.

def go_inicio(request):
    return render(request, 'home.html')

def go_contacto(request):
    return render(request, 'contacto.html')
def log_in(request):
    return render(request, 'log-in.html')

