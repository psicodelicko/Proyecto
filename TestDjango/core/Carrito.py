from urllib import request
from wsgiref.util import request_uri


class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar_producto(self, producto):
        id = str(producto.idProducto)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id" : producto.idProducto,
                "nombre": producto.nombreProducto,
                "acumulado": producto.precioProducto,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.precioProducto
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"]= self.carrito
        self.session.modifield = True

    def eliminar(self, producto):
        id = str(producto.idProducto)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.idProducto)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"]-=1
            self.carrito[id]["acumulado"]-= producto.precioProducto
            if self.carrito[id]["cantidad"] <= 0 : self.eliminar(producto)
            self.guardar_carrito() 

    def limpiar(self):
        self.session["carrito"]= {}
        self.session.modifield = True

    