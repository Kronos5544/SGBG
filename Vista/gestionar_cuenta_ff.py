from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt5 import uic
from Vista.gestionar_cuenta_simp import GestionarCuentaSimple

class GestionarCuentaFormacionFondos(GestionarCuentaSimple, QWidget):
    def __init__(self, presentador):
        self.__presentador = presentador
        QWidget.__init__(self)
        uic.loadUi('./Vista/ui/CRUD_cuentas_formacion_fondos.ui', self) #Cargar ui de la gestión de cuentas de formación de fondos

        self.btn_cerrar.clicked.connect(self.close)
        self.btn_insertar.clicked.connect(self.__presentador.insertar_cuenta_ff)
        self.btn_actualizar.clicked.connect(self.__presentador.actualizar_cuenta_ff)
        self.btn_eliminar.clicked.connect(self.__presentador.eliminar_cuenta_ff)
        self.tabla.itemClicked.connect(self.__presentador.rellenar_form_x_tabla)

        self.tabla.setColumnCount(8)
        self.tabla.setHorizontalHeaderLabels(['Número de cuenta','Cliente', 'Comercial', 'Saldo', 'tipo de moneda', 'fecha de apertura', 'fecha de último retiro', 'cuota mensual'])
        self.tabla.resizeColumnsToContents()

    @property
    def valor_cuota_mensual(self):
        return self.txt_cuota_mensual.text()
    @valor_cuota_mensual.setter
    def valor_cuota_mensual(self, value):
        self.txt_cuota_mensual.setText(value)

    def validar_entradas(self):
        super().validar_entradas()
        if len(self.valor_cuota_mensual) == 0:
            raise Exception('El campo "Cuota Mensual" es obligatorio')
        if self.valor_cuota_mensual.count(".") > 1:
            raise Exception("La cuota mensual es inválido")
        if not self.valor_cuota_mensual.replace(".", "").isdigit():
            raise Exception("La cuota mensual solo puede contener números")  

    def restablecer_valores(self):
        super().restablecer_valores()
        self.valor_cuota_mensual = ""      