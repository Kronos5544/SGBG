from Vista.depositar_retirar import DepositarRetirar

class PresentadorDepRet:
    def __init__(self, banco):
        self.__banco = banco

    def iniciar(self):
        self.__vista = DepositarRetirar(self)
        self.__vista.show()

    def depositar(self):
        try:
            self.__vista.validar_entradas()
            self.__banco.depositar(self.__vista.valor_num_cuenta, float(self.__vista.valor_monto))
            self.__vista.mostrar_información("Depositar", "El depósito se ha realizado correctamente")
        except Exception as error:
            self.__vista.mostrar_error(str(error))

    def retirar(self):
        try:
            self.__vista.validar_entradas()
            self.__banco.retirar(self.__vista.valor_num_cuenta, float(self.__vista.valor_monto))
            self.__vista.mostrar_información("Retirar", "El saldo se ha retirado de la cuenta correctamente")
        except Exception as error:
            self.__vista.mostrar_error(str(error))