from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt5 import uic

class GestionarCuentaSimple(QWidget):
    def __init__(self, presentador):
        self.__presentador = presentador
        super().__init__()
        uic.loadUi('./Vista/ui/CRUD_cuentas_simples.ui', self) #Cargar ui de la gestión de cuentas simples

        self.btn_cerrar.clicked.connect(self.close)
        self.btn_insertar.clicked.connect(self.__presentador.insertar_cuenta_simple)
        self.btn_actualizar.clicked.connect(self.__presentador.actualizar_cuenta_simple)
        self.btn_eliminar.clicked.connect(self.__presentador.eliminar_cuenta_simple)
        self.tabla.itemClicked.connect(self.__presentador.rellenar_form_x_tabla)

        self.tabla.setColumnCount(7)
        self.tabla.setHorizontalHeaderLabels(['Número de cuenta','Cliente', 'Comercial', 'Saldo', 'tipo de moneda', 'fecha de apertura', 'fecha de último retiro'])
        self.tabla.resizeColumnsToContents()

    @property
    def valor_num_cuenta(self):
        return self.txt_num_cuenta.text().strip()
    @valor_num_cuenta.setter
    def valor_num_cuenta(self, value):
        self.txt_num_cuenta.setText(value)

    @property
    def valor_cliente(self):
        return self.txt_cliente.text()
    @valor_cliente.setter
    def valor_cliente(self, value):
        self.txt_cliente.setText(value)

    @property
    def valor_comercial(self):
        return self.txt_comercial.text()
    @valor_comercial.setter
    def valor_comercial(self, value):
        self.txt_comercial.setText(value)

    @property
    def valor_saldo(self):
        return self.txt_saldo.text()
    @valor_saldo.setter
    def valor_saldo(self, value):
        self.txt_saldo.setText(value)

    @property
    def valor_tipo_de_moneda(self):
        if self.rbtn_cup.isChecked():
            moneda = "CUP"
        elif self.rbtn_cuc.isChecked():
            moneda = "CUC"
        elif self.rbtn_usd.isChecked():
            moneda = "USD"
        else:
            moneda = "EUR"
        return moneda
    @valor_tipo_de_moneda.setter
    def valor_tipo_de_moneda(self, value):
        if value == "CUP":
            self.rbtn_cup.setChecked(True)
        elif value == "CUC":
            self.rbtn_cuc.setChecked(True)
        elif value == "USD":
            self.rbtn_usd.setChecked(True)
        else:
            self.rbtn_eur.setChecked(True)

    def agregar_elemento_tabla(self, fila, columna, elemento):
        self.tabla.setItem(fila, columna, QTableWidgetItem(elemento))

    def validar_entradas(self):
        msg = "El campo {} es obligatorio"
        if len(self.valor_num_cuenta) == 0:
            raise Exception(msg.format('"Número de cuenta"'))
        if len(self.valor_num_cuenta) != 16:
            raise Exception("El numéro de cuenta solo puede contener 16 números")
        if not self.valor_num_cuenta.isdigit():
            raise Exception("El número de cuenta solo puede contener números")
        
        if len(self.valor_cliente) == 0:
            raise Exception(msg.format('"Cliente"'))
        
        if len(self.valor_comercial) == 0:
            raise Exception(msg.format('"Comercial"'))
        
        if len(self.valor_saldo) == 0:
            raise Exception(msg.format('"Saldo"'))
        if self.valor_saldo.count(".") > 1:
            raise Exception("El saldo es inválido")
        if not self.valor_saldo.replace(".", "").isdigit():
            raise Exception("El salario solo puede contener números")
        

        


    def vaciar_tabla(self):
        e = self.tabla.rowCount()
        for i in range(e):
            self.tabla.removeRow(0)

    def restablecer_valores(self):
        self.valor_num_cuenta = ""
        self.valor_tipo_de_moneda = "CUP"
        self.valor_cliente = ""
        self.valor_comercial = ""
        self.valor_saldo = ""        

    def mostrar_error(self, error):
        QMessageBox.critical(self, "Error", error)   