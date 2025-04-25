from django.shortcuts import render

# Create your views here.

def go_inicio(request):
    return render(request, 'home2.html')

def log_in(request):
    return render(request, 'log-in.html')
