from Persona import Persona

class Cliente(Persona):
    def __init__(self, centro_trabajo, ocupacion, salario):
        self.__centro_trabajo = centro_trabajo
        self.__ocupacion = ocupacion
        self.__salario = salario
    
    @property
    def centro_trabajo(self):
        return self.__centro_trabajo
    @property
    def ocupacion(self):
        return self.__ocupacion
    @property
    def salario(self):
        return self.__salario
    
    @centro_trabajo.setter
    def centro_trabajo(self, value):
        self.__centro_trabajo = value
    @ocupacion.setter
    def ocupacion(self, value):
        self.__ocupacion = value
    @salario.setter
    def salario(self, value):
        self.__salario = value