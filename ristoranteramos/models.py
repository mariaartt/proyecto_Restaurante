from random import choices

from django.db import models
from django.forms import IntegerField


class Rol(models.TextChoices):
    CAMARERO = 'CAMARERO', 'Camarero'
    COCINERO = 'COCINERO', 'Cocinero'
    ADMINISTRADOR = 'ADMINISTRADOR', 'Administrador'


class Estado_Mesa(models.TextChoices):
    LIBRE = 'LIBRE', 'Libre'
    OCUPADA = 'OCUPADA', 'Ocupada'


class Estado_Pedido(models.TextChoices):
    PENDIENTE = 'PENDIENTE', 'Pendiente'
    EN_PROCESO = 'EN PROCESO', 'En Proceso'
    COMPLETADO = 'COMPLETADO', 'Completado'

class CategoriaProducto(models.TextChoices):
    ENTRANTES = 'ENTRANTES', 'Entrantes'
    COMIDA = 'COMIDA', 'Comida'
    BEBIDA = 'BEBIDA', 'Bebida'
    POSTRES = 'POSTRES', 'Postres'


# Create your models here.
class Articulo(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    precio = models.IntegerField(default=0, null=True)
    categoria = models.CharField(
        max_length=150,
        choices=CategoriaProducto.choices,
        default=CategoriaProducto.COMIDA
    )
    receta = models.TextField(max_length=150, default='Sin receta')
    foto = models.ImageField(upload_to='articulos/', null=True, blank=True)
    tiempo_preparacion = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.nombre


class Mesa(models.Model):
    num_mesa = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=100, choices=Estado_Mesa.choices, default=Estado_Mesa.LIBRE)

    def __str__(self):
        return str(self.num_mesa)


class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    dni = models.CharField(max_length=15)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre


class Empleado(models.Model):
    nombre = models.CharField(max_length=150)
    rol = models.CharField(
        max_length=50,
        choices = Rol.choices,
        default = Rol.CAMARERO
    )

    def __str__(self):
        return self.nombre


# Pedido hecho por cliente o camarero
class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True, null=True, blank=True)
    id_mesa = models.ForeignKey(Mesa, on_delete=models.DO_NOTHING, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    articulo = models.ForeignKey(Articulo, on_delete=models.DO_NOTHING, null=True, blank=True)
    def __str__(self):
        return f"Pedido {self.id_pedido}"


# Tabla intermedia para asociar artículos a un pedido con cantidad
class LineaPedido(models.Model):
    id_linea_pedido = models.AutoField(primary_key=True, null=True, blank=True)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.DO_NOTHING, null=True, blank=True)
    id_articulo = models.ForeignKey(Articulo, on_delete=models.RESTRICT, null=True, blank=True)
    cantidad = models.PositiveIntegerField(default=1)
    fecha_alta = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=100, choices=Estado_Pedido.choices, default=Estado_Pedido.PENDIENTE)

    def __str__(self):
        return f"{self.id_linea_pedido} - {self.id_articulo.nombre if self.id_articulo else 'Sin artículo'} * {self.cantidad}"