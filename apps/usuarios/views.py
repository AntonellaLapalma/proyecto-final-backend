from django.views.generic import TemplateView, View
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .forms import RegistroForm, CustomAuthenticationForm
from apps.productos.models import Categoria, Subcategoria
from apps.carrito.views import CarritoView
from apps.carrito.models import Compra, Detalle_carrito

# No utilice templateview ya que no me mostraba los input de los formularios

class UsuariosView(View):
    template_name='index.html'

    def get(self,request):
        logout(request)
        return redirect('inicio')

class RegistroView(UsuariosView):
    template_name = 'registro.html'

    def get(self, request):
        categorias = Categoria.objects.all()
        subcategorias = Subcategoria.objects.all()
        form = RegistroForm()
        return render(request, self.template_name, {'form': form, 
                                                    'categorias': categorias, 
                                                    'subcategorias': subcategorias})

    def post(self, request):
        categorias = Categoria.objects.all()
        subcategorias = Subcategoria.objects.all()
        form = RegistroForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            password = form.cleaned_data.get('password1')
            user = User.objects.create_user(username=username, first_name=first_name.capitalize(), last_name=last_name.capitalize(), password=password)
            login(request, user)
            return redirect('inicio')
        else:
            print(form.errors)

        return render(request, self.template_name, {'form': form, 
                                                    'categorias': categorias, 
                                                    'subcategorias': subcategorias})

class IniciarSesionView(UsuariosView):
    template_name='iniciar_sesion.html'
    
    def get(self, request):
        categorias = Categoria.objects.all()
        subcategorias = Subcategoria.objects.all()
        form = CustomAuthenticationForm()
        return render(request, self.template_name, {'form': form, 
                                                        'categorias': categorias, 
                                                        'subcategorias': subcategorias})

    def post(self, request):
        categorias = Categoria.objects.all()
        subcategorias = Subcategoria.objects.all()
        error = None

        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = form.get_user()
            login(request, user)
            return redirect('inicio')
        
        else:
            if 'username' not in form.errors:
                error = "Por favor, introduzca un email y clave correctos. Observe que ambos campos pueden ser sensibles a mayúsculas."
            return render(request, self.template_name, {'form': form, 
                                                            'error': error, 
                                                            'categorias': categorias, 
                                                            'subcategorias': subcategorias})

class MisDatosView(UsuariosView):
    template_name='cuenta.html'

    def get(self, request):
        carrito_view = CarritoView()
        carrito = carrito_view.obtener_productos_carrito(request)
        categorias = Categoria.objects.all()
        subcategorias = Subcategoria.objects.all()
        return render(request, self.template_name, {'user': request.user, 
                                                    'categorias': categorias, 
                                                    'subcategorias': subcategorias,
                                                    'productos_carrito': carrito[0], 
                                                    'total_carrito': carrito[1],
                                                    }
                                                )

class MisPedidosView(UsuariosView):
    template_name='pedidos.html'

    def get(self, request, id=None):
        carrito_view = CarritoView()
        carrito = carrito_view.obtener_productos_carrito(request)
        categorias = Categoria.objects.all()
        subcategorias = Subcategoria.objects.all()
        usuario_id = self.request.user.id
        detalle_pedido = ""

        # Obtener los pedidos del usuario actual con los campos deseados
        pedidos = Compra.objects.filter(usuario_id=usuario_id).values('id', 'fecha_creacion', 'cantidad_productos', 'total')
        
        detalles_pedidos = {}
        print(detalles_pedidos)
        if id:
            pedidos = Compra.objects.filter(id=id).values('id', 'fecha_creacion', 'cantidad_productos', 'total')
            detalle_pedido = Detalle_carrito.objects.filter(compra_id=id).values('producto_id', 'producto_nombre', 'cantidad', 'precio_unitario', 'monto_total', 'compra_id')
            detalles_pedidos[id] = detalle_pedido
            print(pedidos)
            print(detalle_pedido)
        return render(request, self.template_name, {'pedidos': pedidos,
                                                    'detalle_pedido': detalle_pedido,
                                                    'productos_carrito': carrito[0], 
                                                    'total_carrito': carrito[1],
                                                    'categorias': categorias, 
                                                    'subcategorias': subcategorias,
                                                    }
                                                )
