from django.shortcuts import render
from apps.productos.models import Categoria, Subcategoria

class Index_views:
    def categorias(request):
        categorias = Categoria.objects.all()
        subcategorias = None

        # Obtiene el parametro de filtrado de la URL
        filtro_categoria = request.POST.get('filtro_categoria')  

        if filtro_categoria:  # Si se proporciona un filtro de categoria
            categoria = Categoria.objects.get(url=filtro_categoria)  # Obtiene la categoria correspondiente
            subcategorias = Subcategoria.objects.filter(categoria=categoria)  # Filtra las subcategorias según la categoria

        return render(request, 'index.html', {'categorias': categorias, 'subcategorias': subcategorias})

