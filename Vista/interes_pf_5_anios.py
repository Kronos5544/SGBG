from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt5 import uic

class InteresPF5Anios(QWidget):
    def __init__(self, presentador):
        self.__presentador = presentador
        super().__init__()
        uic.loadUi('./Vista/ui/interes_plazo_fijo_5a.ui', self) 

        self.tabla.setColumnCount(9)
        self.tabla.setHorizontalHeaderLabels(["Interés acumulado", 'Número de cuenta','Cliente', 'Comercial', 'Saldo', 'tipo de moneda', 'fecha de apertura', 'fecha de último retiro', 'Plazo'])
        self.tabla.resizeColumnsToContents()

    def mostrar_error(self, error):
        return QMessageBox.critical(self, "Error", error)
    
    def agregar_elemento_tabla(self, fila, columna, elemento):
        self.tabla.setItem(fila, columna, QTableWidgetItem(elemento))

    def vaciar_tabla(self):
        e = self.tabla.rowCount()
        for i in range(e):
            self.tabla.removeRow(0)
    