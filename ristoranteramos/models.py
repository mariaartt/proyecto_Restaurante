from random import choices

from django.db import models
from django.forms import IntegerField


class Rol(models.TextChoices):
    CAMARERO = 'CAMARERO', 'Camarero'
    COCINERO = 'COCINERO', 'Cocinero'
    ADMINISTRADOR = 'ADMINISTRADOR', 'Administrador'


# Create your models here.
class Articulo(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    precio = IntegerField()
    categoria = models.CharField(max_length=100)
    receta = models.TextField()
    foto = models.ImageField()
    tiempo_preparacion = models.IntegerField()

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
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    def __str__(self):
        return f"Pedido {self.id}"


# Tabla intermedia para asociar artículos a un pedido con cantidad
class LineaPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.articulo.precio * self.cantidad


    def __str__(self):
        return f"{self.cantidad} x {self.articulo.nombre} en Pedido {self.pedido.id}"