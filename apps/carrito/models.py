from django.db import models
from django.contrib.auth.models import User
from apps.productos.models import Producto

class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    cantidad_productos = models.PositiveIntegerField(default=0)
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    entregado = models.BooleanField(default=False) #entregado / no entregado
    
    def calcular_total(self):
        detalles = self.detalle_carrito_set.all()
        total = sum(detalle.cantidad * detalle.producto.precio for detalle in detalles)
        self.total = total
        self.save()

    def __str__(self):
        return f"Compra - ID: {self.id}"

class Detalle_carrito(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    producto_nombre = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=20, decimal_places=2)
    monto_total = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"{self.producto} - Cantidad: {self.cantidad}"