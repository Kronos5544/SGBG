from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import uic

class CalcularInteres(QWidget):
    def __init__(self, presentador):
        self.__presentador = presentador
        super().__init__()
        uic.loadUi('./Vista/ui/calcular_interes.ui', self)

        self.btn_calcular.clicked.connect(self.__presentador.calcular_interes)

    @property
    def valor_num_cuenta(self):
        return self.txt_numero_cuenta.text().strip()
    
    @valor_num_cuenta.setter
    def valor_num_cuenta(self, value):
        self.txt_num_cuenta.setText(value)

    def validar_entradas(self):
        if len(self.valor_num_cuenta) == 0:
            raise Exception('El campo "Número de cuenta" es obligatorio')
        if not self.valor_num_cuenta.isdigit():
            raise Exception("El número de cuenta solo puede contener números")
        if len(self.valor_num_cuenta) != 16:
            raise Exception("El numéro de cuenta solo puede contener 16 números")
        
    def mostrar_error(self, error):
        return QMessageBox.critical(self, "Error", error)
    
    def mostrar_informacion(self, titulo, msg):
        return QMessageBox.information(self, titulo, msg)