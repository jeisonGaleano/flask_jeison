class Login():

    def __init__(self, usuario, contrasena=None, tipo_usuario=None) -> None:
        self.usuario = usuario
        self.contrasena = contrasena
        self.tipo_usuario=tipo_usuario
    def to_JSON(self):
        return {
            'usuario': self.usuario,
            'contrasena': self.contrasena,
            'tipo_usuario': self.tipo_usuario
        }