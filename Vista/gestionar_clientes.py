from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt5 import uic


class GestionarCliente(QWidget):
    def __init__(self, presentador):
        self.__presentador = presentador
        super().__init__()
        uic.loadUi('./Vista/ui/CRUD_clientes.ui', self) #Cargar ui de la gestión de clientes

        self.btn_cerrar.clicked.connect(self.close)
        self.btn_insertar.clicked.connect(self.__presentador.insertar_cliente)
        self.btn_actualizar.clicked.connect(self.__presentador.actualizar_cliente)
        self.btn_eliminar.clicked.connect(self.__presentador.eliminar_cliente)
        self.tabla.itemClicked.connect(self.__presentador.rellenar_form_x_tabla)

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
        return self.txt_centro_trabajo.text().strip()
    
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

        if len(self.valor_centro_trab) == 0:
            raise Exception(msg.format('"Centro de Trabajo"'))
        
        if len(self.valor_ocup) == 0:
            raise Exception(msg.format('"Ocupación"'))
        
        if len(self.valor_salario) == 0:
            raise Exception(msg.format('"Salario"'))
        if self.valor_salario.count(".") > 1:
            raise Exception("El salario es inválido")
        if not self.valor_salario.replace(".", "").isdigit():
            raise Exception("El salario solo puede contener números")

        
    def restablecer_valores(self):
        self.valor_nombre = ""
        self.valor_sexo = "M"
        self.valor_ci = ""
        self.valor_centro_trab = ""
        self.valor_ocup = ""
        self.valor_salario = ""
  

    def mostrar_error(self, error):
        QMessageBox.critical(self, "Error", error)
        

