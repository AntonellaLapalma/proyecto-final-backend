from django.contrib import admin
from .models import Producto, Categoria, Subcategoria

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # lista los productos y llama las columnas declaradas entre ()
    list_display=('id','categoria','subcategoria','marca','modelo','stock','precio','titulo_publicacion','imagen_publicacion')
    # filtra los productos y segun lo declarado entre ()
    list_filter=('categoria','subcategoria','marca','modelo')
    # barra de busqueda para buscar productos segun lo declarado entre ()
    search_fields=('id','categoria','subcategoria','marca','modelo')
    # habilita la edicion de los campos declarados entre ()
    list_editable=('categoria','subcategoria','marca','modelo','stock','precio','titulo_publicacion','imagen_publicacion')

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == 'sub_categoria':
    #         form_field = super().formfield_for_foreignkey(db_field, request, **kwargs)
    #         categoria_id = request.GET.get('categoria')
    #         producto_id = request.path.split("/")[-3]
    #         productos=Producto.objects.get(id=producto_id)
    #         print("--------")
    #         # print(dir(db_field))
    #         # print(db_field.__dict__)
    #         # print(db_field.id)
    #         print("+++++++++")
    #         # print(form_field.__dict__)
    #         print(dir(request))
    #         print(request.path.split("/")[-3])
    #         print("--------")
    #         print(categoria_id)
    #         # if categoria_id:
    #         #     form_field.queryset = Producto().subcategorias_por_categoria(categoria_id)
    #         # else:
    #         #     form_field.queryset = Subcategoria.objects.none()
    #         # return form_field
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display=('nombre', 'url',)
    readonly_fields = ('url',)

@admin.register(Subcategoria)
class SubcategoriaAdmin(admin.ModelAdmin):
    list_display=('categoria','nombre', 'url',)
    list_filter=('categoria','nombre',)
    search_fields=('categoria','nombre',)
    readonly_fields = ('url',)
