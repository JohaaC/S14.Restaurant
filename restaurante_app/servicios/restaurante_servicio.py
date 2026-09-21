from pathlib import Path

from servicios.archivo_servicio import (
    ArchivoServicio
)


class RestauranteServicio:

    def __init__(self):

        base_dir = Path(__file__).resolve().parent.parent

        self.ruta_productos = (
            base_dir / "datos" / "productos.json"
        )

        self.ruta_usuarios = (
            base_dir / "datos" / "usuarios.json"
        )

        self.archivo_servicio = ArchivoServicio()

    # -------------------------
    # USUARIOS
    # -------------------------

    def obtener_usuarios(self):

        return self.archivo_servicio.leer_json(
            self.ruta_usuarios
        )

    def validar_usuario(
        self,
        usuario,
        contraseña
    ):

        usuarios = self.obtener_usuarios()

        for usuario_data in usuarios:

            if (
                usuario_data.get("usuario") == usuario
                and usuario_data.get("contraseña") == contraseña
            ):

                return True

        return False

    # -------------------------
    # PRODUCTOS
    # -------------------------

    def obtener_productos(self):

        return self.archivo_servicio.leer_json(
            self.ruta_productos
        )

    def guardar_productos(self, productos):

        self.archivo_servicio.guardar_json(
            self.ruta_productos,
            productos
        )

    def obtener_siguiente_id(self):

        productos = self.obtener_productos()

        if not productos:
            return 1

        ids = [
            producto.get("id", 0)
            for producto in productos
        ]

        return max(ids) + 1

    def registrar_producto(
        self,
        nombre,
        categoria,
        precio,
        cantidad
    ):

        productos = self.obtener_productos()

        nuevo_producto = {
            "id": self.obtener_siguiente_id(),
            "nombre": nombre,
            "categoria": categoria,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }

        productos.append(nuevo_producto)

        self.guardar_productos(productos)

        return nuevo_producto

    def actualizar_producto(
        self,
        id_producto,
        nombre,
        categoria,
        precio,
        cantidad
    ):

        productos = self.obtener_productos()

        for producto in productos:

            if producto.get("id") == id_producto:

                producto["nombre"] = nombre
                producto["categoria"] = categoria
                producto["precio"] = float(precio)
                producto["cantidad"] = int(cantidad)

                self.guardar_productos(productos)

                return True

        return False

    def eliminar_producto(self, id_producto):

        productos = self.obtener_productos()

        productos_actualizados = [
            producto
            for producto in productos
            if producto.get("id") != id_producto
        ]

        if len(productos_actualizados) == len(productos):

            return False

        self.guardar_productos(
            productos_actualizados
        )

        return True