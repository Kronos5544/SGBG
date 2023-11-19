from CuentaSimple import CuentaSimple

class CuentaFF(CuentaSimple):
<<<<<<< HEAD
    def __init__(self, num_cuenta, cliente, datos_comercial, saldo, tipo_moneda, fecha_apertura, fecha_ult_retiro, cuota_mensual):
        super().__init__(num_cuenta, cliente, datos_comercial, saldo, tipo_moneda, fecha_apertura, fecha_ult_retiro)
=======
    def __init__(self, cuota_mensual):
>>>>>>> master
        self.__cuota_mensual = cuota_mensual
    
    @property
    def cuota_mensual(self):
        return self.__cuota_mensual
    @cuota_mensual.setter
    def cuota_mensual(self, value):
        self.__cuota_mensual = value