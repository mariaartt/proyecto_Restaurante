from os.path import pathsep

from django.urls import path
from ristoranteramos.views import *

urlpatterns = [
    path('', go_home, name='inicio'),
    path('home/', go_home, name='home'),
    path('contacto/', go_contacto, name='contacto'),
    path('newEmpleado/', new_empleado, name='new_empleado'),
    path('newArticulo/', new_articulo, name='new_articulo'),
    path('verArticulos', go_articulos, name='articulos'),
    path('verEmpleados/', go_empleados, name='empleados'),
    path('login/', go_login, name='login'),
]