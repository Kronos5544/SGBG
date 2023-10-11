from CuentaSimple import CuentaSimple

class CuentaFF(CuentaSimple):
    def __init__(self, num_cuenta, cliente, datos_comercial, saldo, saldo_cup, tipo_moneda, fecha_apertura, fecha_ult_retiro, cuota_mensual):
        super().__init__(num_cuenta, cliente, datos_comercial, saldo, saldo_cup, tipo_moneda, fecha_apertura, fecha_ult_retiro)
        self.__cuota_mensual = cuota_mensual
    
    @property
    def cuota_mensual(self):
        return self.__cuota_mensual
    @cuota_mensual.setter
    def cuota_mensual(self, value):
        self.__cuota_mensual = value