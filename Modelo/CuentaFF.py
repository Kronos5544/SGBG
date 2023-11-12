from CuentaSimple import CuentaSimple

class CuentaFF(CuentaSimple):
    def __init__(self, cuota_mensual):
        self.__cuota_mensual = cuota_mensual
    
    @property
    def cuota_mensual(self):
        return self.__cuota_mensual
    @cuota_mensual.setter
    def cuota_mensual(self, value):
        self.__cuota_mensual = value