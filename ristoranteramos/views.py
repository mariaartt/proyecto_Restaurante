from django.shortcuts import render

# Create your views here.

def go_inicio(request):
    return render(request, 'base.html')

