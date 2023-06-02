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
from apps.home.views import Index_views
from apps.productos.views import Productos_views
from apps.clientes.views import Clientes_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index_views.categorias),
    path('buscar/', Productos_views.buscar_productos, name='buscar'),
    path('categorias/<str:filtro_categoria>/', Productos_views.mostrar_productos, name='mostrar_productos'),
    path('categorias/<str:filtro_categoria>/<str:filtro_subcategoria>/', Productos_views.mostrar_productos_subcategoria, name='mostrar_productos_subcategoria'),
    path('login/', Clientes_views.iniciar_sesion, name='login'),
]
