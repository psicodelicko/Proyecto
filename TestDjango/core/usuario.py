
class Usuario:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        usuario = self.session.get("usuario")
        if not usuario:
            self.session["usuario"] = {}
            self.usuario = self.session["usuario"]
        else:
            self.usuario = usuario

    def agregar(self, usuario):
        id = str(usuario.idUsuario)
        self.usuario[id] = {
            "idUsuario" : usuario.idUsuario,
            "nombres": usuario.nombres,
            "apellidos": usuario.apellidos,
            "nombreUsuario" : usuario.nombreUsuario
        }
        self.guardar()
    
    def guardar(self):
        self.session["usuario"]= self.usuario
        self.session.modifield = True
    
    def limpiar(self):
        self.session["usuario"]= {}
        self.session.modifield = True