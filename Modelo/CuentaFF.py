from Modelo.CuentaSimple import CuentaSimple
from datetime import date

class CuentaFF(CuentaSimple):
    def __init__(self, num_cuenta, cliente, datos_comercial, saldo, tipo_moneda, fecha_apertura, fecha_ult_retiro, cuota_mensual):
        super().__init__(num_cuenta, cliente, datos_comercial, saldo, tipo_moneda, fecha_apertura, fecha_ult_retiro)
        self.__cuota_mensual = cuota_mensual
    
    @property
    def cuota_mensual(self):
        return self.__cuota_mensual
    @cuota_mensual.setter
    def cuota_mensual(self, value):
        self.__cuota_mensual = value

    def calcularInteres(self):
        interes = 0
        hoy = date.today()
        anios = hoy.year - self.fecha_ult_retiro.year
          
        if self.fecha_ult_retiro.month > hoy.month:
            anios -= 1
        elif self.fecha_ult_retiro.month == hoy.month and self.fecha_ult_retiro.day > hoy.day:
            anios -= 1
        if anios < 0:
            anios = 0

        interes = (self.saldo * 0.06) * anios

        return interes