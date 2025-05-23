from os.path import pathsep

from django.template.context_processors import static
from django.urls import path

from restaurante import settings
from ristoranteramos.views import *

urlpatterns = [
    path('', go_home, name='inicio'),
    path('home/', go_home, name='home'),
    path('contacto/', go_contacto, name='contacto'),
    path('verEmpleados/', go_empleados, name='empleados'),
    path('newEmpleado/<int:id>', editar_empleado, name='new_empleado'),
    path('eliminarEmpleado/<int:id>', eliminar_empleado, name='eliminar_empleado'),
    path('verArticulos/', go_articulos, name='articulos'),
    path('newArticulo/<int:id>', editar_articulo, name='new_articulo'),
    path('eliminarArticulo/<int:id>', eliminar_articulo, name='eliminar_articulo'),
    path('log-in/', log_in, name='log_in_page'),
    path('carta/', go_carta, name='carta'),
    path('login/', go_login, name='login'),
    path('reporte/', go_reporte_ventas, name='reporte'),
    path('acerca_de/', go_acerca_de, name='acerca_de'),
]


