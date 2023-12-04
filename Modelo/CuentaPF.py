from Modelo.CuentaSimple import CuentaSimple
from datetime import date

class CuentaPF(CuentaSimple):
    def __init__(self, num_cuenta, cliente, datos_comercial, saldo, tipo_moneda, fecha_apertura, fecha_ult_retiro, plazo):
        super().__init__(num_cuenta, cliente, datos_comercial, saldo, tipo_moneda, fecha_apertura, fecha_ult_retiro)
        self.__plazo = plazo
    
    @property
    def plazo(self):
        return self.__plazo
    @plazo.setter
    def plazo(self, value):
        self.__plazo = value

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

        if anios >= 5:
            interes = self.saldo * 0.16

        elif anios >= 1:
            interes = self.saldo * (0.08 + (0.02 * (anios - 1)))

        else:
            interes = 0

        return interes
        