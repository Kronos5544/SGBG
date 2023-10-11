from CuentaSimple import CuentaSimple

class CuentaPL(CuentaSimple):
    def __init__(self, plazo):
        self.__plazo = plazo
    
    @property
    def plazo(self):
        return self.__plazo
    @plazo.setter
    def plazo(self, value):
        self.__plazo = value