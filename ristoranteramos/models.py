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

class Empleado(models.Model):

    nombre = models.CharField(max_length=150)
    rol = models.CharField(
        max_length=50,
        choices = Rol.choices,

        default = ''
    )

    def __str__(self):
        return self.nombre

# Pedido hecho por cliente o camarero
class Pedido(models.Model):

    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id}"

    # def total(self):
    #     return sum(linea.subtotal() for linea in self.lineapedido_set.all())


# Tabla intermedia para asociar artículos a un pedido con cantidad
class LineaPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.articulo.precio * self.cantidad

    def __str__(self):
        return f"{self.cantidad} x {self.articulo.nombre} en Pedido {self.pedido.id}"