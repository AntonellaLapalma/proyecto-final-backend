from django.shortcuts import render
from .models import Producto, Categoria, Subcategoria

class Productos_views:
    @staticmethod
    def mostrar_productos(request, filtro_categoria):
        # Busca y muestra productos en la tabla productos según la categoría solicitada
        productos = Producto.objects.filter(categoria=(filtro_categoria.replace("-", " ")).title())
        categorias = Categoria.objects.all()
        subcategorias = Subcategoria.objects.all()
        rutas = [(filtro_categoria.replace("-", " ")).title()]
        return render(request, 'mostrar_productos.html', {'categorias': categorias, 'subcategorias': subcategorias, 'productos': productos, 'filtro_categoria':filtro_categoria,'rutas':rutas})
    
    @staticmethod
    def mostrar_productos_subcategoria(request, filtro_categoria, filtro_subcategoria):
        # Busca y muestra productos en la tabla productos según la categoría y subcategoría solicitada
        productos = Producto.objects.filter(categoria=(filtro_categoria.replace("-", " ")).title(), marca=filtro_subcategoria.capitalize())
        categorias = Categoria.objects.all()
        subcategorias = Subcategoria.objects.all()
        rutas = [(filtro_categoria.replace("-", " ")).title(), (filtro_subcategoria.replace("-", " ")).title()]
        return render(request, 'mostrar_productos.html', {'categorias': categorias, 'subcategorias': subcategorias, 'productos': productos, 'filtro_categoria':filtro_categoria, 'filtro_subcategoria':filtro_subcategoria, 'rutas':rutas})
    
    @staticmethod
    def buscar_productos(request):
        #busca productos segun la palabra ingresada y los titulos de publicacion
        if request.method == 'GET':
            categorias = Categoria.objects.all()
            subcategorias = Subcategoria.objects.all()
            texto = request.GET.get('item')  # Obtengo el texto de búsqueda
            productos = Producto.objects.filter(titulo_publicacion__icontains=texto)
            rutas = [texto.title()]
            return render(request, 'mostrar_productos.html', {'categorias': categorias, 'subcategorias': subcategorias, 'productos': productos, 'filtro_categoria':request,'rutas':rutas})