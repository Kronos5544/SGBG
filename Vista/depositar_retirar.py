from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import uic

class DepositarRetirar(QWidget):
    def __init__(self, presentador):
        super().__init__()
        self.__presentador = presentador
        uic.loadUi('./Vista/ui/depositar.ui', self)

        self.btn_depositar.clicked.connect(self.__presentador.depositar)
        self.btn_retirar.clicked.connect(self.__presentador.retirar)

    @property
    def valor_num_cuenta(self):
        return self.txt_numero_cuenta.text().strip()
    @valor_num_cuenta.setter
    def valor_num_cuenta(self, value):
        self.txt_numero_cuenta.setText(value)

    @property
    def valor_monto(self):
        return self.txt_monto.text()
    @valor_monto.setter
    def valor_monto(self, value):
        self.txt_monto.setText(value)

    def validar_entradas(self):
        if len(self.valor_num_cuenta) == 0:
            raise Exception('El campo "Número de cuenta" es obligatorio')
        if not self.valor_num_cuenta.isdigit():
            raise Exception("El número de cuenta solo puede contener números")
        if len(self.valor_num_cuenta) != 16:
            raise Exception("El numéro de cuenta solo puede contener 16 números")
        
        if len(self.valor_monto) == 0:
            raise Exception('El campo "Monto" es obligatorio')
        if self.valor_monto[0] == "-" :
            raise Exception("El monto no puede ser negativo")
        if self.valor_monto.count(".") > 1:
            raise Exception("El monto es inválido")
        if not self.valor_monto.replace(".", "").isdigit():
            raise Exception("El monto solo puede contener números")
        if float(self.valor_monto) == 0:
            raise Exception('El monto no puede ser 0')

    def mostrar_información(self, titulo, msg):
        return QMessageBox.information(self, titulo, msg)
    
    def mostrar_error(self, error):
        return QMessageBox.critical(self, "Error", error)