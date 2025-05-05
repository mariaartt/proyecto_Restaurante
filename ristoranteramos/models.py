from django.contrib.auth.models import AbstractUser
from django.db import models

# ----------------------
# MODELOS DE USUARIOS
# ----------------------

ROLES = (
    ('administrador', 'Administrador'),
    ('camarero', 'Camarero/a'),
    ('cocinero', 'Cocinero/a'),
    ('cliente', 'Cliente'),
)

class Usuario(AbstractUser):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    rol = models.CharField(max_length=20, choices=ROLES, default='cliente')
    foto = models.ImageField(upload_to='perfiles/', blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.CharField(max_length=255, blank=True)

    REQUIRED_FIELDS = ['email']

class HistorialInicioSesion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()

# ----------------------
# MODELOS DEL RESTAURANTE
# ----------------------

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class ArticuloCarta(models.Model):
    nombre = models.CharField(max_length=100)
    ingredientes = models.CharField(max_length=1000)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='carta/', null=True, blank=True)
    receta = models.TextField()
    tiempo_estimado = models.PositiveIntegerField(help_text="Tiempo en minutos")

class Mesa(models.Model):
    numero = models.PositiveIntegerField(unique=True)
    disponible = models.BooleanField(default=True)

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