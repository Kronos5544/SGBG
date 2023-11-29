from Vista.gestionar_comerciales import GestionarComercial

class PresentadorComercial:
    def __init__(self, banco):
        self.__banco = banco
        

    def iniciar(self):
        self.__vista = GestionarComercial(self)
        self.__vista.show()
