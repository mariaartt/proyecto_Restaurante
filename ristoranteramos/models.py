from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from random import choices

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.forms import IntegerField


# ----------------------
# MODELOS DE USUARIOS
# ----------------------
class UsuarioManager(BaseUserManager):
    def create_user(self, email, nombre, rol, password=None):
        if not email:
            raise ValueError("El usuario debe tener un email")
        email = self.normalize_email(email)
        usuario = self.model(email=email, nombre=nombre, rol=rol)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

class Rol(models.TextChoices):
    CLIENTE = 'CLIENTE', 'Cliente'
    CAMARERO = 'CAMARERO', 'Camarero'
    COCINERO = 'COCINERO', 'Cocinero'
    ADMINISTRADOR = 'ADMINISTRADOR', 'Administrador'

    def create_superuser(self, email, nombre, rol='admin', password=None):
        usuario = self.create_user(email, nombre, rol, password)
        usuario.is_superuser = True
        usuario.is_staff = True
        usuario.save(using=self._db)
        return usuario

ROLES = (
    ('administrador', 'Administrador'),
    ('camarero', 'Camarero/a'),
    ('cocinero', 'Cocinero/a'),
    ('cliente', 'Cliente'),
)

class Usuario(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    rol = models.CharField(max_length=20, choices=ROLES, default='cliente')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='perfiles/', blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.CharField(max_length=255, blank=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'rol']

    def __str__(self):
        return self.email

class HistorialInicioSesion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()

# ----------------------
# MODELOS DEL RESTAURANTE
# ----------------------

CATEGORIAS = (
    ('per_iniziare', 'Per Iniziare'),
    ('pasta_fresca', 'Pasta Fresca'),
    ('pizzas', 'Pizzas'),
    ('bebidas', 'Bebidas'),
    ('vinos', 'Vinos'),
    ('cafe_postres', 'Café y Postres'),
)

class ArticuloCarta(models.Model):
    nombre = models.CharField(max_length=100)
    ingredientes = models.CharField(max_length=1000)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    foto = models.ImageField(upload_to='carta/', null=True, blank=True)
    receta = models.TextField()
    tiempo_estimado = models.PositiveIntegerField(help_text="Tiempo en minutos")

    def __str__(self):
        return self.nombre

class Mesa(models.Model):
    numero = models.PositiveIntegerField(unique=True)
    disponible = models.BooleanField(default=True)

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

# MODELOS DE USUARIOS
# ----------------------
# class UsuarioManager(BaseUserManager):
#     def create_user(self, email, nombre, rol, password=None):
#         if not email:
#             raise ValueError("El usuario debe tener un email")
#
#         email = self.normalize_email(email)
#         usuario = self.model(email=email, nombre=nombre, rol=rol)
#         usuario.set_password(password)
#         usuario.save(using=self._db)
#         return usuario
#
#     def create_superuser(self, email, nombre, rol='admin', password=None):
#         usuario = self.create_user(email, nombre, rol, password)
#
#         usuario.is_superuser = True
#         usuario.is_staff = True
#         usuario.save(using=self._db)
#         return usuario
#
#
# class Usuario(AbstractBaseUser, PermissionsMixin):
#     nombre = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     rol = models.CharField(max_length=20, choices=Rol, default='cliente')
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     foto = models.ImageField(upload_to='perfiles/', blank=True, null=True)
#     telefono = models.CharField(max_length=15, blank=True)
#     direccion = models.CharField(max_length=255, blank=True)
#
#     objects = UsuarioManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['nombre', 'rol']
#
#     def __str__(self):
#         return self.email
#
#
# class HistorialInicioSesion(models.Model):
#     usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
#     fecha_hora = models.DateTimeField(auto_now_add=True)
#     ip = models.GenericIPAddressField()

#MODELOS DEL RESTAURANTE

class Articulo(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    precio = models.IntegerField(default=0, null=True)
    categoria = models.CharField(
        max_length=150,
        choices=CategoriaProducto.choices,
        default=CategoriaProducto.COMIDA
    )
    receta = models.TextField(default='Sin receta')
    foto = models.ImageField(upload_to='articulos/', null=True, blank=True)
    tiempo_preparacion = models.IntegerField(default=0, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"Mesa {self.numero}"

# ----------------------
# MODELOS DE PEDIDOS
# ----------------------

ESTADO_PEDIDO = (
    ('pendiente', 'Pendiente'),
    ('preparado', 'Preparado'),
    ('servido', 'Servido'),
    ('pagado', 'Pagado'),
)

class Pedido(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'rol': 'cliente'})
    mesa = models.ForeignKey(Mesa, on_delete=models.SET_NULL, null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_PEDIDO, default='pendiente')
    fecha_hora = models.DateTimeField(auto_now_add=True)

class LineaPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='lineas')
    articulo = models.ForeignKey(ArticuloCarta, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('preparado', 'Preparado')], default='pendiente')

# ----------------------
# MODELOS DE FACTURACIÓN
# ----------------------

class Factura(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

class Mesa(models.Model):
    num_mesa = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=100, choices=Estado_Mesa.choices, default=Estado_Mesa.LIBRE)

    def __str__(self):
        return str(self.num_mesa)


# Pedido hecho por cliente o camarero
# class Pedido(models.Model):
#     id_mesa = models.ForeignKey(Mesa, on_delete=models.DO_NOTHING, null=True, blank=True)
#     fecha = models.DateTimeField(auto_now_add=True)
#     articulo = models.ForeignKey(Articulo, on_delete=models.DO_NOTHING, null=True, blank=True)
#     def __str__(self):
#         return f"Pedido {self.id_pedido}"
#
#
# # Tabla intermedia para asociar artículos a un pedido con cantidad
# class LineaPedido(models.Model):
#     id_pedido = models.ForeignKey(Pedido, on_delete=models.DO_NOTHING, null=True, blank=True)
#     id_articulo = models.ForeignKey(Articulo, on_delete=models.RESTRICT, null=True, blank=True)
#     cantidad = models.PositiveIntegerField(default=1)
#     fecha_alta = models.DateField(null=True, blank=True)
#     estado = models.CharField(max_length=100, choices=Estado_Pedido.choices, default=Estado_Pedido.PENDIENTE)
#
#     def __str__(self):
#         return f"{self.id_linea_pedido} - {self.id_articulo.nombre if self.id_articulo else 'Sin artículo'} * {self.cantidad}"

