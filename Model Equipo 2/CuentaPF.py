from CuentaSimple import CuentaSimple

class CuentaPL(CuentaSimple):
    def __init__(self, num_cuenta, cliente, datos_comercial, saldo, saldo_cup, tipo_moneda, fecha_apertura, fecha_ult_retiro, plazo):
        super().__init__(num_cuenta, cliente, datos_comercial, saldo, saldo_cup, tipo_moneda, fecha_apertura, fecha_ult_retiro)
        self.__plazo = plazo
    
    @property
    def plazo(self):
        return self.__plazo
    @plazo.setter
    def plazo(self, value):
        self.__plazo = value