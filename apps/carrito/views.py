from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from apps.productos.models import Producto, Categoria, Subcategoria
from .models import Compra, Detalle_carrito
from .utils import Carro
from django.contrib.auth.models import User

class CarritoView(TemplateView):
    template_name = 'carrito.html'

    def obtener_productos_carrito(self, request):
        carro = Carro(request)
        productos_carrito = []
        for producto_id, item in carro.carro.items():
            productos_carrito.append({
                'id': item['producto_id'],
                'producto': item['nombre'],
                'imagen': item['imagen'],
                'cantidad': item['cantidad'],
                'precio': item['precio'],
                'subtotal': float(item['precio']) * item['cantidad']
            })

        total_carrito = sum(item['subtotal'] for item in productos_carrito)

        return productos_carrito, total_carrito
    
    def get(self, request):
        categorias = Categoria.objects.all()
        subcategorias = Subcategoria.objects.all()
        productos_carrito, total_carrito = self.obtener_productos_carrito(request)

        return render(request, self.template_name, {'productos_carrito': productos_carrito,
                                                    'total_carrito': total_carrito,
                                                    'categorias': categorias,
                                                    'subcategorias': subcategorias
                                                    })

    def post(self, request, producto_id=None):
        if not request.user.is_authenticated:
            # No hay sesión activa, redirigir a la página de inicio de sesión
            return redirect('iniciar_sesion')

        accion = request.POST.get('accion', '')
        carro = Carro(request)

        if accion == 'agregar':
            producto = Producto.objects.get(id=producto_id)
            carro.agregar(producto)
        elif accion == 'restar':
            producto = Producto.objects.get(id=producto_id)
            carro.modificar(producto, 'restar')
        elif accion == 'eliminar':
            carro.eliminar(producto_id)
        elif accion == 'finalizar_compra':
            carro = Carro(request)
            username = request.user.username
            user = User.objects.get(username=username)

            compra = Compra(usuario=user)
            compra.save()

            for producto_id, item in carro.carro.items():
                producto = Producto.objects.get(id=producto_id)
                detalle_carrito = Detalle_carrito(compra=compra, producto=producto, producto_nombre=item['nombre'],cantidad=item['cantidad'], precio_unitario=item['precio'], monto_total=str(float(item['precio'])*float(item['cantidad'])))
                detalle_carrito.save()

            compra.calcular_total()

            carro.limpiar()
            return redirect('confirmacion_compra')

        url_referencia = request.META.get('HTTP_REFERER')

        return redirect(url_referencia)
    
class ConfirmacionCompraView(TemplateView):
    template_name = 'confirmacion_compra.html'

    def get(self, request):
        # Obtener la última compra realizada por el usuario actual
        compra = Compra.objects.filter(usuario=request.user).latest('fecha_creacion')
        categorias = Categoria.objects.all()
        subcategorias = Subcategoria.objects.all()

        return render(request, self.template_name, {'compra': compra,
                                                    'categorias': categorias,
                                                    'subcategorias': subcategorias
                                                    })