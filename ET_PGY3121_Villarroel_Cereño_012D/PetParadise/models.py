import datetime
from django.db import models
from django.conf import settings


class Tienda(models.Model):
    codigo = models.CharField(primary_key=True, max_length=8, verbose_name="Codigo")
    descripcion = models.CharField(max_length=500, blank=True, verbose_name="Descripcion")
    precio = models.IntegerField(blank=True, null=True, verbose_name="Precio")
    stock = models.IntegerField(blank=True, verbose_name="Stock")
    imagen = models.ImageField(upload_to="imagenes", null=True, blank=True, verbose_name="Imagen")

    def __str__(self):
        return self.codigo


class Boleta(models.Model):
    ESTADO_CHOICES = (
        ('PP', 'Procesando Pedido'),
        ('ENP', 'En Proceso'),
        ('ENT', 'Entregado'),
        ('CAN', 'Cancelado'),
    )
    id_boleta = models.AutoField(primary_key=True)
    total = models.BigIntegerField()
    fechaCompra = models.DateTimeField(blank=False, null=False, default=datetime.datetime.now)
    estado = models.CharField(max_length=3, choices=ESTADO_CHOICES, default='PP')

    def __str__(self):
        return str(self.id_boleta)


class detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Tienda', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)

