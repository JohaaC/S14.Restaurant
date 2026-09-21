class Producto:

    def __init__(
        self,
        id_producto,
        nombre,
        categoria,
        precio,
        cantidad
    ):
        self.id = id_producto
        self.nombre = nombre
        self.categoria = categoria
        self.precio = float(precio)
        self.cantidad = int(cantidad)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "cantidad": self.cantidad
        }