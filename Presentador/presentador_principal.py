import sys
from PyQt5.QtWidgets import QApplication
from Modelo.Banco import Banco
from Presentador.presentador_clientes import PresentadorCliente
from Vista.ventana_principal import MainWindow
from Vista.acerca_de import AcercaDe

class PresentadorPrincipal:
    def __init__(self):
        self.__banco = Banco()

#Iniciar Ventana Principal
    def iniciar(self):
        app = QApplication(sys.argv)
        self.__vista = MainWindow(self)
        self.__vista.show()
        app.exec()

#Iniciar acerca de
    def acerca_de(self):
        acerca_de = AcercaDe()
        acerca_de.exec()

#Iniciar Gestionar clientes
    def crud_clientes(self):
        crud_clientes = PresentadorCliente(self.__banco)
        crud_clientes.iniciar()

    def cargar_BD(self):
        self.__banco.CargarBDCliente()