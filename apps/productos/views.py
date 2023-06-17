from .models import Producto, Categoria, Subcategoria
from apps.carrito.views import CarritoView
from apps.home.views import IndexView
from django.db.models import Q # Q permite construir consultas complejas de filtro utilizando operadores lógicos como OR (|) y AND (&)


class ProductosView(IndexView):
    template_name = 'mostrar_productos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filtro_categoria = self.kwargs.get('filtro_categoria')
        filtro_subcategoria = self.kwargs.get('filtro_subcategoria')

        carrito_view = CarritoView()
        carrito = carrito_view.obtener_productos_carrito(self.request)
        context['productos_carrito'] = carrito[0]
        context['total_carrito'] = carrito[1]

        categorias = Categoria.objects.all()
        subcategorias = Subcategoria.objects.all()
        context['categorias'] = categorias
        context['subcategorias'] = subcategorias

        productos = Producto.objects.filter(stock__gt=0)  # Filtrar solo productos con stock mayor a 0, __gt significa mayor que

        if filtro_categoria and filtro_subcategoria:
            productos = productos.filter(
                categoria=(filtro_categoria.replace("-", " ")).title(),
                subcategoria=(filtro_subcategoria.replace("-", " ")).title()
            )
            rutas = [(filtro_categoria.replace("-", " ")).title(), (filtro_subcategoria.replace("-", " ")).title()]
            context['filtro_categoria'] = filtro_categoria
            context['filtro_subcategoria'] = filtro_subcategoria
            context['rutas'] = rutas

        elif filtro_categoria:
            productos = productos.filter(
                categoria=(filtro_categoria.replace("-", " ")).title()
            )
            rutas = [(filtro_categoria.replace("-", " ")).title()]
            context['filtro_categoria'] = filtro_categoria
            context['rutas'] = rutas
            
        elif self.request.method == 'GET' and 'item' in self.request.GET:
            # En las busquedas devolvera los productos que su titulo o marca o categoria o subcategoria coincidan con la busqueda
            texto = self.request.GET.get('item')
            productos = productos.filter(
                Q(titulo_publicacion__icontains=texto) |
                Q(marca__icontains=texto) |
                Q(modelo__icontains=texto) |
                Q(categoria__nombre__icontains=texto) |
                Q(subcategoria__nombre__icontains=texto)
            ).distinct()  # resultados únicos
            rutas = [texto.title()]
            context['filtro_categoria'] = texto
            context['rutas'] = rutas

        context['productos'] = productos
        return context
    

# | or
# gt (mayor que)
# lt (menor que)
# gte (mayor o igual que)
# lte (menor o igual que)
# exact (igual a)
# contains (contiene)
# icontains (contiene, sin distinción entre mayúsculas y minúsculas)