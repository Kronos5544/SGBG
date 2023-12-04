from datetime import date

class CuentaSimple:
    def __init__(self, num_cuenta, cliente, datos_comercial, saldo, tipo_moneda, fecha_apertura, fecha_ult_retiro):
        self.__num_cuenta = num_cuenta
        self.__cliente = cliente
        self.__datos_comercial = datos_comercial
        self.__saldo = saldo
        self.__saldo_cup = 0
        self.__tipo_moneda = tipo_moneda
        self.__fecha_apertura = date.fromisoformat(fecha_apertura)
        self.__fecha_ult_retiro = date.fromisoformat(fecha_ult_retiro)
        
    @property
    def num_cuenta(self):
        return self.__num_cuenta
    @property
    def cliente(self):
        return self.__cliente
    @property
    def datos_comercial(self):
        return self.__datos_comercial
    @property
    def saldo(self):
        return self.__saldo
    @property
    def saldo_cup(self):
        return self.__saldo_cup
    @property
    def tipo_moneda(self):
        return self.__tipo_moneda
    @property
    def fecha_apertura(self):
        return self.__fecha_apertura
    @property
    def fecha_ult_retiro(self):
        return self.__fecha_ult_retiro
    
    @num_cuenta.setter
    def num_cuenta(self, value):
        self.__num_cuenta = value
    @cliente.setter
    def cliente(self,value):
        self.__cliente = value
    @datos_comercial.setter
    def datos_comercial(self,value):
        self.__datos_comercial = value
    @saldo.setter
    def saldo(self,value):
        self.__saldo = value
    @saldo_cup.setter
    def saldo_cup(self,value):
        self.__saldo_cup = value
    @tipo_moneda.setter
    def tipo_moneda(self,value):
        self.__tipo_moneda = value
    @fecha_apertura.setter
    def fecha_apertura(self,value):
        self.__fecha_apertura = date.fromisoformat(value)
    @fecha_ult_retiro.setter
    def fecha_ult_retiro(self,value):
        self.__fecha_ult_retiro = date.fromisoformat(value)

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

        interes = (self.saldo * 0.04) * anios
        return interes