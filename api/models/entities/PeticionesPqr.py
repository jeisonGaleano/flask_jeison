class PeticionesPqr():

    def __init__(self, usuario, correo = None, mensaje = None) -> None:
        self.usuario = usuario
        self.correo = correo
        self.mensaje=mensaje
    def to_JSON(self):
        return {
            'usuario': self.usuario,
            'correo': self.correo,
            'mensaje': self.mensaje
        }