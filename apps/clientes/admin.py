from django.contrib import admin
from apps.clientes.models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display=('dni', 'nombre', 'apellido', 'celular', 'email', 'activo')
    search_fields=('dni', 'nombre', 'apellido')
    list_editable=('nombre', 'apellido', 'celular', 'email', 'activo')
    
admin.site.register(Cliente,ClienteAdmin)