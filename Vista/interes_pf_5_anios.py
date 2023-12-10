from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt5.QtCore import QDate
from PyQt5 import uic

class InteresPF5Anios(QWidget):
    def __init__(self, presentador):
        self.__presentador = presentador
        super().__init__()
        uic.loadUi('./Vista/ui/interes_plazo_fijo_5a.ui', self)

        self.btn_mostrar.clicked.connect(self.__presentador.interes_pf_5_anios)
        self.tabla.setColumnCount(9)
        self.tabla.setHorizontalHeaderLabels(["Interés acumulado", 'Número de cuenta','Cliente', 'Comercial', 'Saldo', 'tipo de moneda', 'fecha de apertura', 'fecha de último retiro', 'Plazo'])
        self.tabla.resizeColumnsToContents()

    @property
    def valor_fecha_creacion(self):
        return self.fecha_creacion.date().toString('yyyy-MM-dd')
    @valor_fecha_creacion.setter
    def valor_fecha_creacion(self, value):
        value = QDate.fromString(value, "yyyy-MM-dd")
        self.fecha_creacion.setDate(value)

    def mostrar_error(self, error):
        return QMessageBox.critical(self, "Error", error)
    
    def agregar_elemento_tabla(self, fila, columna, elemento):
        self.tabla.setItem(fila, columna, QTableWidgetItem(elemento))

    def vaciar_tabla(self):
        e = self.tabla.rowCount()
        for i in range(e):
            self.tabla.removeRow(0)
    