from os.path import pathsep

from django.template.context_processors import static
from django.urls import path

from restaurante import settings
from ristoranteramos.views import *

urlpatterns = [
    path('', go_home, name='inicio'),
    path('home/', go_home, name='home'),
    path('contacto/', go_contacto, name='contacto'),
    path('carta/', cargar_listado_articulos, name='carta'),
    path('login/', go_login, name='login'),
    path('reporte/', go_reporte_ventas, name='reporte')
]
