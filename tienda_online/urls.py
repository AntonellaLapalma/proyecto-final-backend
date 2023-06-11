"""tienda_online URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.home.views import PaginaPrinciaplView
from apps.productos.views import ProductosView
from apps.usuarios.views import UsuariosView, IniciarSesionView, RegistroView, MisDatosView, MisPedidosView
from apps.carrito.views import CarritoView, ConfirmacionCompraView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', PaginaPrinciaplView.as_view(), name='inicio'),

    path('buscar/', ProductosView.buscar_productos, name='buscar'),
    path('categorias/<str:filtro_categoria>/', ProductosView.mostrar_productos, name='mostrar_productos'),
    path('categorias/<str:filtro_categoria>/<str:filtro_subcategoria>/', ProductosView.mostrar_productos_subcategoria, name='mostrar_productos_subcategoria'),

    path('iniciar_sesion/', IniciarSesionView.as_view(), name='iniciar_sesion'),
    path('registro/', RegistroView.as_view(), name='registrar'),
    path('cuenta/', MisDatosView.as_view(), name='mis_datos'),
    path('pedidos/', MisPedidosView.as_view(), name='pedidos'),
    path('pedidos/<int:id>/', MisPedidosView.as_view(), name='detalle_pedido'),
    path('cerrar_sesion/', UsuariosView.as_view(), name='cerrar_sesion'),

    path('agregar-al-carrito/<int:producto_id>/', CarritoView.as_view(), name='agregar_al_carrito'),
    path('carrito/', CarritoView.as_view(), name='carrito'),
    path('carrito/<int:producto_id>/', CarritoView.as_view(), name='modificar_carrito'),
    path('carrito/<int:producto_id>/eliminar/', CarritoView.as_view(), name='eliminar_del_carrito'),
    path('finalizar-compra/', CarritoView.as_view(), name='finalizar_compra'),
    path('confirmacion_compra/', ConfirmacionCompraView.as_view(), name='confirmacion_compra'),
]
