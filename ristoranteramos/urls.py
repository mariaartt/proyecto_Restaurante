from os.path import pathsep

from django.urls import path
from ristoranteramos.views import *

urlpatterns = [

    path('', go_inicio, name='inicio'),
    path('inicio/', go_inicio, name='inicio_page'),
    path('log-in/', log_in, name='log_in_page'),
]