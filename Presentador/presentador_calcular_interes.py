from Vista.calcular_interes import CalcularInteres

class PresentadorCalcInteres:
    def __init__(self, banco):
        self.__banco = banco
        
    def iniciar(self):
        self.__vista = CalcularInteres(self)
        self.__vista.show()

    def calcular_interes(self):
        try:
            self.__vista.validar_entradas()
            interes = self.__banco.calcularInteresxNum(self.__vista.valor_num_cuenta)
            self.__vista.mostrar_informacion("Interes Calculado", f"El interés de la cuenta {self.__vista.valor_num_cuenta} es de {interes[0]} {interes[1]}")
        except Exception as error:
            self.__vista.mostrar_error(str(error))