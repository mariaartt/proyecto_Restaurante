from os.path import pathsep

from django.urls import path
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
    path('login/', go_login, name='login'),
]