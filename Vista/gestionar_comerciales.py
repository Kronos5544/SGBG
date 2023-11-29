from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt5 import uic

class GestionarComercial(QWidget):
    def __init__(self, presentador):
        self.__presentador = presentador
        super().__init__()
        uic.loadUi('./Vista/ui/CRUD_comerciales.ui', self) #Cargar ui de la gestión de comerciales

        self.btn_cerrar.clicked.connect(self.close)
        """self.btn_insertar.clicked.connect(self.__presentador.insertar_comercial)
        self.btn_actualizar.clicked.connect(self.__presentador.actualizar_comercial)
        self.btn_eliminar.clicked.connect(self.__presentador.eliminar_comercial)
        self.tabla.itemClicked.connect(self.__presentador.rellenar_form_x_tabla)"""

        self.tabla.setColumnCount(4)
        self.tabla.setHorizontalHeaderLabels(['Nombre','Sexo', 'CI', 'años de experiencia'])
        self.tabla.resizeColumnsToContents()