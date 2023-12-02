import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from Modelo.Banco import Banco
from Presentador.presentador_clientes import PresentadorCliente
from Presentador.presentador_comerciales import PresentadorComercial
from Presentador.presentador_cuentas_simples import PresentadorCuentaSimple
from Presentador.presentador_cuentas_pf import PresentadorCuentaPF
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

#Guarda los clientes, comerciales y las cuentas creadas en ese momento, llamando a dichas funciones del modelo. Además de que muestra una ventana al usuario, preguntándole si está seguro de que desea realizar la operación
    def guardar_BD(self):
        try:
            selec = self.__vista.alerta("Guardar", "¿Está seguro de que desea guardar los cambios? Se sobreescribirán los datos anteriores") #Carga una ventana que le pregunta al usuario si está seguro de que desea efectuar la operación, dependiendo de la desición del usuario la funcion devolverá True o False
            if selec:
                self.__banco.GuardarBDCliente()
                self.__banco.GuardarBDComercial()
                self.__banco.GuardarBDCuentaSimp()
                self.__banco.GuardarBDCuentaFF()
                self.__banco.GuardarBDCuentaPF()
        except Exception:
            self.__vista.mostrar_error("Ha ocurrido un error al guardar la Base de Datos")

#Carga los clientes, comerciales y cuentas que hay guardadas en la base de datos. Además de que muestra una ventana al usuario preguntándole si está seguro de que deasea efecectuar dicha operación
    def cargar_BD(self):
        try:
            selec = self.__vista.alerta("Cargar", "¿Está seguro de que desea cargar la Base de Datos? Perderá los cambios que no haya guardado") #Carga una ventana que le pregunta al usuario si está seguro de que desea efectuar la operación, dependiendo de la desición del usuario la funcion devolverá True o False
            if selec:
                self.__banco.CargarBDCliente()
                self.__banco.CargarBDComercial()
                self.__banco.CargarBDCuentaSimp()
                self.__banco.CargarBDCuentaFF()
                self.__banco.CargarBDCuentaPF()
        except Exception:
            self.__vista.mostrar_error("Ha ocurrido un error al cargar la Base de Datos")

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
    
#Iniciar Gestionar cuentas de Plazo Fijo
    def crud_cuentas_pf(self):
        crud_cuentas_pf = PresentadorCuentaPF(self.__banco)
        crud_cuentas_pf.iniciar()