from os.path import pathsep

from django.urls import path
from ristoranteramos.views import *

urlpatterns = [
    path('', go_home, name='inicio'),
    path('home/', go_home, name='home'),
    path('contacto/', go_contacto, name='contacto'),
    path('log-in/', log_in, name='log_in_page'),
]