from Vista.gestionar_clientes import GestionarCliente

class PresentadorCliente:
    def __init__(self, banco):
        self.__banco = banco

#Cargar ventana desde la vista
    def iniciar(self):
        self.__vista = GestionarCliente(self)
        self.__vista.show()