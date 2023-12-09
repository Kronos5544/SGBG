from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt5 import uic

class CuentasPFMas10MilPesos(QWidget):
    def __init__(self, presentador):
        super().__init__()
        self.__presentador = presentador
        uic.loadUi('./Vista/ui/cuenta_plazo_fijo_+10mil.ui', self)

        self.tabla.setColumnCount(9)
        self.tabla.setHorizontalHeaderLabels(['Número de cuenta','Cliente', 'Comercial', 'Saldo en CUP', 'Saldo', 'tipo de moneda', 'fecha de apertura', 'fecha de último retiro', 'Plazo'])
        self.tabla.resizeColumnsToContents()


    def mostrar_error(self, error):
        return QMessageBox.critical(self, "Error", error)
    
    def agregar_elemento_tabla(self, fila, columna, elemento):
        self.tabla.setItem(fila, columna, QTableWidgetItem(elemento))

    def vaciar_tabla(self):
        e = self.tabla.rowCount()
        for i in range(e):
            self.tabla.removeRow(0)
