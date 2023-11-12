from Persona import Persona

class Comercial(Persona):
    def __init__(self, anios_ex):
        self.__anios_ex = anios_ex

    @property
    def anios_ex(self):
        return self.__anios_ex
    @anios_ex.setter
    def anios_ex(self, valve):
        self.__anios_ex = valve        