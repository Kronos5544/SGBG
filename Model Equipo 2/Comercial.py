from Persona import Persona

class Comercial(Persona):
    def __init__(self,nombre, sexo, ci, anios_ex):
        super().__init__(nombre, sexo, ci)
        self.__anios_ex = anios_ex

    @property
    def anios_ex(self):
        return self.__anios_ex
    @anios_ex.setter
    def anios_ex(self, valve):
        self.__anios_ex = valve        