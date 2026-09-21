class Usuario:

    def __init__(
        self,
        usuario,
        contraseña,
        nombre
    ):
        self.usuario = usuario
        self.contraseña = contraseña
        self.nombre = nombre

    def to_dict(self):
        return {
            "usuario": self.usuario,
            "contraseña": self.contraseña,
            "nombre": self.nombre
        }