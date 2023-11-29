from Vista.gestionar_cuenta_simp import GestionarCuentaSimple
from Modelo.CuentaSimple import CuentaSimple

class PresentadorCuentaSimple:
    def __init__(self, banco):
        self.__banco = banco

    def iniciar(self):
        self.__vista = GestionarCuentaSimple(self)
        self.__vista.show()