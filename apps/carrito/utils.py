class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = {}
        self.carro = carro

    def agregar(self, producto):
        producto_id = str(producto.id)
        if producto_id not in self.carro:
            self.carro[producto_id] = {
                "producto_id": producto_id,
                "nombre": producto.titulo_publicacion,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen_publicacion.url
            }
        else:
            self.carro[producto_id]["cantidad"] += 1
        self.guardar_carro()
    
    def modificar(self, producto, accion):
        producto_id = str(producto.id)
        print(producto_id)
        if producto_id in self.carro:
            if accion == 'agregar':
                self.carro[producto_id]['cantidad'] += 1
            elif accion == 'restar':
                if self.carro[producto_id]['cantidad'] > 1:
                    self.carro[producto_id]['cantidad'] -= 1
                else:
                    del self.carro[producto_id]
            self.guardar_carro()

    def eliminar(self, producto):
        producto_id = str(producto)
        if producto_id in self.carro:
            del self.carro[producto_id]
            self.guardar_carro()

    def limpiar(self):
        self.carro = {}
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True