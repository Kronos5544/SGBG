from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt5 import uic


class GestionarCliente(QWidget):
    def __init__(self, presentador):
        self.__presentador = presentador
        super().__init__()
        uic.loadUi('./Vista/ui/CRUD_clientes.ui', self) #Cargar ui de la gestión de clientes

        self.btn_cerrar.clicked.connect(self.close)
        self.btn_insertar.clicked.connect(self.__presentador.insertar_cliente)

        self.tabla.setColumnCount(6)
        self.tabla.setHorizontalHeaderLabels(['Nombre','Sexo', 'CI', 'Centro de Trabajo', 'Ocupación', 'Salario'])
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
            self.rbtn_mas.setChecked(True)
            
        
    @property
    def valor_ci(self):
        return self.txt_ci.text().strip()
        
    @valor_ci.setter
    def valor_ci(self, value):
        self.txt_ci.setText(value)
    

    @property
    def valor_centro_trab(self):
        return self.txt_centro_trabajo.text().strip().capitalize()
    
    @valor_centro_trab.setter
    def valor_centro_trab(self, value):
        self.txt_centro_trabajo.setText(value)


    @property
    def valor_ocup(self):
        return self.txt_ocupacion.text().strip()

    @valor_ocup.setter
    def valor_ocup(self, value):
        self.txt_ocupacion.setText(value)


    @property
    def valor_salario(self):
        return self.txt_salario.text().strip()
    
    @valor_salario.setter
    def valor_salario(self, value):
        self.txt_salario.setText(value)

    
    
    def vaciar_tabla(self):
        e = self.tabla.rowCount()
        for i in range(e):
            self.tabla.removeRow(0)

    def agregar_elemento_tabla(self, fila, columna, elemento):
        self.tabla.setItem(fila, columna, QTableWidgetItem(elemento))
        

