from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt5 import uic

class GestionarCuentaSimple(QWidget):
    def __init__(self, presentador):
        self.__presentador = presentador
        super().__init__()
        uic.loadUi('./Vista/ui/CRUD_cuentas_simples.ui', self) #Cargar ui de la gestión de comerciales