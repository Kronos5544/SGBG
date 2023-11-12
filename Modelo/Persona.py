class Persona:
    def __init__(self, nombre, sexo, ci):
        self.__nombre = nombre
        self.__sexo = sexo
        self.__ci = ci

    @property
    def nombre(self):
        return self.__nombre
    @property
    def sexo(self):
        return self.__sexo
    @property
    def ci(self):
        return self.__ci

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value
    @sexo.setter 
    def sexo(self, value):
        self.__sexo = value
    @ci.setter
    def ci (self , value):
        self.__ci = value