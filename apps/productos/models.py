from django.db import models
from unidecode import unidecode

class Categoria(models.Model):
    nombre = models.CharField(primary_key=True,max_length=30, verbose_name='categoría')
    url = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        # guarda el nombre en minuscula sin espacios
        self.url = unidecode(self.nombre).replace(" ", "-").lower()
        super().save(*args, **kwargs)

    def __str__(self):
        # muestra el nombre de la categoria
        return self.nombre
    
class Subcategoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, verbose_name='subcategoría')
    url = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        # guarda el nombre en minuscula sin espacios
        self.url = unidecode(self.nombre).replace(" ", "-").lower()
        super().save(*args, **kwargs)

    def __str__(self):
        # muestra el nombre de la subcategoria
        return self.nombre

class Producto(models.Model):
    id = models.BigIntegerField(primary_key=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='categoría')
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE, null=True, blank=True, verbose_name='sub categoría')
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    titulo_publicacion = models.CharField(max_length=100)
    stock = models.IntegerField()
    precio = models.IntegerField()
    imagen_publicacion = models.ImageField(upload_to='img/', default='default.jpg')
    
    # def subcategorias_por_categoria(self, categoria_id):
    #     if categoria_id:
    #         return Subcategoria.objects.filter(categoria_id=categoria_id)
    #     return Subcategoria.objects.none()
    
    # @property
    # def categorias_producto(self):
    #     return Subcategoria.objects.filter(categoria_id=self.categoria.id)