from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QCloseEvent, QResizeEvent
from PyQt5 import uic
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self, presentador):
        self.__presentador = presentador
        QMainWindow.__init__(self)
        uic.loadUi('Vista/ui/ventana_principal.ui', self)

        self.setWindowIcon(QIcon('Vista/media/icon/gangdec png ico.ico'))
        self.actionSalir.triggered.connect(self.close) #Cerrar ventana al presionar salir
        self.actionAcerca_de.triggered.connect(self.__presentador.acerca_de) #Cargar la ventana acerca de al presionar botón acerca de
        self.actionClientes.triggered.connect(self.__presentador.crud_clientes) #Cargar la ventana de gestión de clientes
        self.actionComerciales.triggered.connect(self.__presentador.crud_comerciales) #Cargar la ventana de gestión de clientes
        self.actionCuentas_Simples.triggered.connect(self.__presentador.crud_cuentas_simples) #Cargar la ventana de gestión de cuentas simples
        self.actionCuentas_de_Plazo_Fijo.triggered.connect(self.__presentador.crud_cuentas_pf) #Cargar la ventana de gestión de cuentas de plazo fijo
        self.actionCuentas_de_Formacion_de_Fondos.triggered.connect(self.__presentador.crud_cuentas_ff) #Cargar la ventana de gestión de cuentas de Formación de Fondos
        self.actionCalcular_Interes.triggered.connect(self.__presentador.calcular_interes) #Cargar la ventana de calcular interés
        self.actionDepositar.triggered.connect(self.__presentador.depositar_retirar) #Cargar la ventana de Depositar y Retirar
        self.actionInteres_Plazo_Fijo_5a.triggered.connect(self.__presentador.interes_pf_5_anios) #Cargar la ventana de calcular interés pf en 5 años
        self.actionPropietario_Cuenta_Mayor_Saldo.triggered.connect(self.__presentador.prop_cuenta_may_saldo) #Cargar la ventana del propietarop de la cuenta de mayor saldo
        self.actionCuenta_Plazo_Fijo_mas_10mil.triggered.connect(self.__presentador.cuentas_pf_mas_10_mil) #Cargar la ventana de Cuentas PF con más de 10 mil CUP
        self.actionGuardar.triggered.connect(self.__presentador.guardar_BD)
        self.actionCargar.triggered.connect(self.__presentador.cargar_BD)

    def resizeEvent(self, a0: QResizeEvent):
        logo = QPixmap('./Vista/media/logo.png')
        logo = logo.scaled(self.size(), Qt.IgnoreAspectRatio)  # KeepAspectRatio, KeepAspectRatioByExpanding
        pal = self.palette()
        pal.setBrush(QPalette.Background, QBrush(logo))
        self.setPalette(pal)


    def alerta(self,nombre_ventana, msg):
        ventana = QMessageBox.question(self, nombre_ventana,  msg, QMessageBox.Yes | QMessageBox.No)
        if ventana == QMessageBox.Yes:
            return True
        else: 
            return False
        
    def mostrar_error(self, error):
        QMessageBox.critical(self, "Error", error)


    def closeEvent(self, a0: QCloseEvent):
        QMainWindow.closeEvent(self, a0)

