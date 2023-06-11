from django.views.generic import TemplateView
from django.shortcuts import render
from apps.productos.models import Categoria, Subcategoria
from apps.carrito.views import CarritoView

class IndexView(TemplateView):
    template_name='index.html'

class PaginaPrinciaplView(IndexView):
    template_name='contenido_index.html'
    def get(self,request):
        categorias = Categoria.objects.all()
        subcategorias = None
        carrito_view = CarritoView()
        carrito = carrito_view.obtener_productos_carrito(request)
        # Obtiene el parametro de filtrado de la URL
        filtro_categoria = request.POST.get('filtro_categoria')  

        if filtro_categoria:  # Si se proporciona un filtro de categoria
            categoria = Categoria.objects.get(url=filtro_categoria)  # Obtiene la categoria correspondiente
            subcategorias = Subcategoria.objects.filter(categoria=categoria)  # Filtra las subcategorias según la categoria

        return render(request, self.template_name, {'categorias': categorias, 
                                                    'subcategorias': subcategorias,
                                                    'productos_carrito': carrito[0], 
                                                    'total_carrito': carrito[1],
                                                    })

