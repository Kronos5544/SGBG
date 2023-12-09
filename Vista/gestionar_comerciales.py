from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt5 import uic

class GestionarComercial(QWidget):
    def __init__(self, presentador):
        self.__presentador = presentador
        super().__init__()
        uic.loadUi('./Vista/ui/CRUD_comerciales.ui', self) #Cargar ui de la gestión de comerciales

        self.btn_cerrar.clicked.connect(self.close)
        self.btn_insertar.clicked.connect(self.__presentador.insertar_comercial)
        self.btn_actualizar.clicked.connect(self.__presentador.actualizar_comercial)
        self.btn_eliminar.clicked.connect(self.__presentador.eliminar_comercial)
        self.tabla.itemClicked.connect(self.__presentador.rellenar_form_x_tabla)

        self.tabla.setColumnCount(4)
        self.tabla.setHorizontalHeaderLabels(['Nombre','Sexo', 'CI', 'años de experiencia'])
        self.tabla.resizeColumnsToContents()

    @property
    def valor_nombre(self):
        return self.txt_nombre.text().strip().title()
    
    @valor_nombre.setter
    def valor_nombre(self, value):
        self.txt_nombre.setText(value)


    @property
    def valor_sexo(self):
        if self.rbtn_mas.isChecked():
            sex = "M"
        else:
            sex = "F"
        return sex    

    @valor_sexo.setter
    def valor_sexo(self, value):
        if value == "M":
            self.rbtn_mas.setChecked(True)
        else:
            self.rbtn_fem.setChecked(True)
            
        
    @property
    def valor_ci(self):
        return self.txt_ci.text().strip()
        
    @valor_ci.setter
    def valor_ci(self, value):
        self.txt_ci.setText(value)


    @property
    def valor_annios_ex(self):
        return self.spn_anios_ex.value()
    
    @valor_annios_ex.setter
    def valor_annios_ex(self, value):
        self.spn_anios_ex.setValue(value)

    def agregar_elemento_tabla(self, fila, columna, elemento):
        self.tabla.setItem(fila, columna, QTableWidgetItem(elemento))

    def validar_entradas(self):
        msg = "El campo {} es obligatorio"
        if len(self.valor_nombre) == 0:
            raise Exception(msg.format('"Nombre"'))
        if not self.valor_nombre.replace(" ", "").isalpha():
            raise Exception("El Nombre solo puede contener letras")

        if len(self.valor_ci) == 0:
            raise Exception(msg.format('"Carnet de Identidad"'))
        if not self.valor_ci.isdigit():
            raise Exception("El Carnet de Identidad solo puede contener números")
        if len(self.valor_ci) != 11:
            raise Exception("El Carnet de Identidad tiene que tener 11 números")
        
        if self.valor_annios_ex > 100:
            raise Exception("Los años de experiencia no pueden ser mayor que 100")
        
        
    def vaciar_tabla(self):
        e = self.tabla.rowCount()
        for i in range(e):
            self.tabla.removeRow(0)


    def restablecer_valores(self):
        self.valor_nombre = ""
        self.valor_sexo = "M"
        self.valor_ci = ""
        self.valor_annios_ex = 0


    def mostrar_error(self, error):
        QMessageBox.critical(self, "Error", error)