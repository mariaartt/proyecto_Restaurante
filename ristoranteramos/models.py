from random import choices

from django.db import models
from django.forms import IntegerField
from django.utils.functional import empty


class Rol(models.TextChoices):
    CAMARERO = 'CAMARERO', 'Camarero'
    COCINERO = 'COCINERO', 'Cocinero'
    ADMINISTRADOR = 'ADMINISTRADOR', 'Administrador'


# Create your models here.
class Articulo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    precio = IntegerField()
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


