class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, nombre, cantidad, precio):
        self.productos[nombre] = {"cantidad": cantidad, "precio": precio}

    def actualizar_producto(self, nombre, cantidad=None, precio=None):
        if nombre in self.productos:
            if cantidad is not None:
                self.productos[nombre]["cantidad"] = cantidad
            if precio is not None:
                self.productos[nombre]["precio"] = precio

    def eliminar_producto(self, nombre):
        if nombre in self.productos:
            del self.productos[nombre]

    def obtener_producto(self, nombre):
        if nombre in self.productos:
            return {"nombre": nombre, **self.productos[nombre]}
        else:
            raise KeyError("El producto no existe")

    def listar_productos(self):
        return [{"nombre": nombre, **detalles} for nombre, detalles in self.productos.items()]
