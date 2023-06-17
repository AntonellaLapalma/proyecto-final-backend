from django.contrib import admin
from .models import Compra, Detalle_carrito

# Register your models here.
@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    # lista los productos y llama las columnas declaradas entre ()
    list_display=('usuario','fecha_creacion','cantidad_productos','total','entregado')
    # filtra los productos y segun lo declarado entre ()
    list_filter=('usuario','fecha_creacion','entregado')
    # barra de busqueda para buscar productos segun lo declarado entre ()
    search_fields=('usuario','fecha_creacion')

@admin.register(Detalle_carrito)
class Detalle_carritoAdmin(admin.ModelAdmin):
    # lista los productos y llama las columnas declaradas entre ()
    list_display=('compra','producto','producto_nombre','cantidad','precio_unitario','monto_total')
    # filtra los productos y segun lo declarado entre ()
    list_filter=('compra','producto','producto_nombre')
    # barra de busqueda para buscar productos segun lo declarado entre ()
    search_fields=('compra','producto','producto_nombre')
