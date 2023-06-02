from django.shortcuts import render
from apps.productos.models import Categoria, Subcategoria #es necesario importar para que el menu siga funcionando

class Clientes_views:
    @staticmethod
    def iniciar_sesion(request):
        categorias = Categoria.objects.all()
        subcategorias = Subcategoria.objects.all()
        return render(request, 'login.html', {'categorias': categorias, 'subcategorias': subcategorias})