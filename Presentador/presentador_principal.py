import sys
from PyQt5.QtWidgets import QApplication
from Vista.ventana_principal import MainWindow
from Modelo.Banco import Banco

class PresentadorPrincipal:
    def __init__(self):
        self.__banco = Banco()

    def iniciar(self):
        app = QApplication(sys.argv)
        self.__vista = MainWindow(self)
        self.__vista.show()
        app.exec()
