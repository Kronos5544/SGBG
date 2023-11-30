import sys
from PyQt5.QtWidgets import QApplication
from Modelo.Banco import Banco
from Presentador.presentador_clientes import PresentadorCliente
from Presentador.presentador_comerciales import PresentadorComercial
from Presentador.presentador_cuentas_simples import PresentadorCuentaSimple
from Presentador.presentador_cuentas_ff import PresentadorCuentaFF
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
        self.__banco.CargarBDComercial()
        self.__banco.CargarBDCuentaSimp()
        self.__banco.CargarBDCuentaFF()

#Iniciar Gestionar comerciales
    def crud_comerciales(self):
        crud_comerciales = PresentadorComercial(self.__banco)
        crud_comerciales.iniciar()

#Iniciar Gestionar cuentas simples
    def crud_cuentas_simples(self):
        crud_cuentas_simples = PresentadorCuentaSimple(self.__banco)
        crud_cuentas_simples.iniciar()

#Iniciar Gestionar cuentas de formación de fondos
    def crud_cuentas_ff(self):
        crud_cuentas_ff = PresentadorCuentaFF(self.__banco)
        crud_cuentas_ff.iniciar()