from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QCloseEvent, QResizeEvent
from PyQt5 import uic

class MainWindow(QMainWindow):
    def __init__(self, presentador):
        self.__presentador = presentador
        QMainWindow.__init__(self)
        uic.loadUi('Vista/ui/ventana_principal.ui', self)

        self.actionSalir.triggered.connect(self.close) #Cerrar ventana al presionar salir
        self.actionAcerca_de.triggered.connect(self.__presentador.acerca_de) #Cargar la ventana acerca de al presionar botón acerca de
        self.actionClientes.triggered.connect(self.__presentador.crud_clientes) #Cargar la ventana de gestión de clientes
        self.actionComerciales.triggered.connect(self.__presentador.crud_comerciales) #Cargar la ventana de gestión de clientes
        self.actionCuentas_Simples.triggered.connect(self.__presentador.crud_cuentas_simples) #Cargar la ventana de gestión de cuentas simples
        self.actionCuentas_de_Plazo_Fijo.triggered.connect(self.__presentador.crud_cuentas_pf) #Cargar la ventana de gestión de cuentas de plazo fijo
        self.actionCuentas_de_Formacion_de_Fondos.triggered.connect(self.__presentador.crud_cuentas_ff) #Cargar la ventana de gestión de cuentas de Formación de Fondos
        self.actionGuardar.triggered.connect(self.__presentador.guardar_BD)
        self.actionCargar.triggered.connect(self.__presentador.cargar_BD)

    def resizeEvent(self, a0: QResizeEvent):
        logo = QPixmap('./Vista/media/logo.png')
        logo = logo.scaled(self.size(), Qt.IgnoreAspectRatio)  # KeepAspectRatio, KeepAspectRatioByExpanding
        pal = self.palette()
        pal.setBrush(QPalette.Background, QBrush(logo))
        self.setPalette(pal)


    def closeEvent(self, a0: QCloseEvent):
        QMainWindow.closeEvent(self, a0)

    def alerta_guardar(self):
        msg = QMessageBox.question(self,"Guardar",  "¿Está seguro de que desea guardar los cambios? Se sobreescribirán los datos anteriores", QMessageBox.Yes | QMessageBox.No)
        if msg == QMessageBox.Yes:
            return True
        else: 
            return False
        
    def alerta_cargar(self):
        msg = QMessageBox.question(self,"Cargar",  "¿Está seguro de que desea cargar la Base de Datos? Perderá los cambios que no haya guardado", QMessageBox.Yes | QMessageBox.No)
        if msg == QMessageBox.Yes:
            return True
        else: 
            return False   
        
    def mostrar_error(self, error):
        QMessageBox.critical(self, "Error", error)

