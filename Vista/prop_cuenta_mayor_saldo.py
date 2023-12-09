from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt5 import uic

class PropCuentaMayorSaldo(QWidget):
    def __init__(self, presentador):    
        super().__init__()
        self.__presentador = presentador
        uic.loadUi('./Vista/ui/propietario_cuenta_mayor_saldo.ui', self)

        self.tabla.setColumnCount(9)
        self.tabla.setHorizontalHeaderLabels(['Nombre','Sexo', 'CI', 'Centro de Trabajo', 'Ocupación', 'Salario', "Número de Cuenta", "Saldo con intereses", "Tipo de moneda"])
        self.tabla.resizeColumnsToContents()


    def mostrar_error(self, error):
        return QMessageBox.critical(self, "Error", error)
    
    def agregar_elemento_tabla(self, fila, columna, elemento):
        self.tabla.setItem(fila, columna, QTableWidgetItem(elemento))

    def vaciar_tabla(self):
        e = self.tabla.rowCount()
        for i in range(e):
            self.tabla.removeRow(0)