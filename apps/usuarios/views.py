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

    def get_context_data(self):
        categorias = Categoria.objects.all()
        subcategorias = Subcategoria.objects.all()
        carrito_view = CarritoView()
        carrito = carrito_view.obtener_productos_carrito(self.request)

        context = {
            'categorias': categorias,
            'subcategorias': subcategorias,
            'productos_carrito': carrito[0],
            'total_carrito': carrito[1],
        }
        return context

    def get(self,request):
        logout(request)
        return redirect('inicio')

class RegistroView(UsuariosView):
    template_name = 'registro.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('inicio')
        form = RegistroForm()
        context = self.get_context_data()
        context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request):
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

        context = self.get_context_data()
        context['form'] = form
        return render(request, self.template_name, context)

class IniciarSesionView(UsuariosView):
    template_name='iniciar_sesion.html'
    
    def get(self, request):
        if request.user.is_authenticated: #si el usuario ya ingreso no podra ver esta ventana ni la de registro
            return redirect('inicio')
        form = CustomAuthenticationForm()
        context = self.get_context_data()
        context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request):
        error = ''
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('inicio')
        
        else:
            if 'username' not in form.errors:
                error = "Por favor, introduzca un email y clave correctos. Observe que ambos campos pueden ser sensibles a mayúsculas."
        
        context = self.get_context_data()
        context['form'] = form
        context['error'] = error
        return render(request, self.template_name, context)

class MisDatosView(UsuariosView):
    template_name='cuenta.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('inicio')
        else:
            context = self.get_context_data()
            context['user'] = request.user
            return render(request, self.template_name, context)

class MisPedidosView(UsuariosView):
    template_name='pedidos.html'

    def get(self, request, id=None):
        if not request.user.is_authenticated:
            return redirect('inicio')
        else:
            context = super().get_context_data()
            context['id'] = id

            # Obtener los pedidos del usuario 
            usuario_id = self.request.user.id
            pedidos = Compra.objects.filter(usuario_id=usuario_id).values('id', 'fecha_creacion', 'cantidad_productos', 'total')

            detalle_pedido = None
            detalles_pedidos = {}

            if id:
                total = Compra.objects.filter(id=id).values('total')
                detalle_pedido = Detalle_carrito.objects.filter(compra_id=id).values('producto_id', 'producto_nombre', 'cantidad', 'precio_unitario', 'monto_total', 'compra_id')
                detalles_pedidos[id] = detalle_pedido

                context['pedido_total'] = total
            context['pedidos'] = pedidos
            context['detalle_pedido'] = detalle_pedido
            context['detalles_pedidos'] = detalles_pedidos

            return render(request, self.template_name, context)
