import sys
from PyQt5.QtWidgets import QApplication
from Modelo.Banco import Banco
from Vista.ventana_principal import MainWindow
from Vista.acerca_de import AcercaDe

class PresentadorPrincipal:
    def __init__(self):
        self.__banco = Banco()

    def iniciar(self):
        app = QApplication(sys.argv)
        self.__vista = MainWindow(self)
        self.__vista.show()
        app.exec()

    def acerca_de(self):
        acerca_de = AcercaDe()
        acerca_de.exec()
