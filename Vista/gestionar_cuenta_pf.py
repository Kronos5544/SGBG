from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt5 import uic
from Vista.gestionar_cuenta_simp import GestionarCuentaSimple

class GestionarCuentaPlazoFijo(GestionarCuentaSimple, QWidget):
    def __init__(self, presentador):
        self.__presentador = presentador
        QWidget.__init__(self)
        uic.loadUi('./Vista/ui/CRUD_cuentas_plazo_fijo.ui', self) #Cargar ui de la gestión de cuentas de plazo fijo

        self.btn_cerrar.clicked.connect(self.close)
        self.btn_insertar.clicked.connect(self.__presentador.insertar_cuenta_pf)
        self.btn_actualizar.clicked.connect(self.__presentador.actualizar_cuenta_pf)
        self.btn_eliminar.clicked.connect(self.__presentador.eliminar_cuenta_pf)
        self.tabla.itemClicked.connect(self.__presentador.rellenar_form_x_tabla)

        self.tabla.setColumnCount(8)
        self.tabla.setHorizontalHeaderLabels(['Número de cuenta','Cliente', 'Comercial', 'Saldo', 'tipo de moneda', 'fecha de apertura', 'fecha de último retiro', 'Plazo'])
        self.tabla.resizeColumnsToContents()

    def validar_entradas(self):
        super().validar_entradas()
        if self.valor_plazo < 1 or self.valor_plazo > 5:
            raise Exception("El plazo tiene que ser un valor entre 1 y 5")

    @property
    def valor_plazo(self):
        return self.spn_plazo.value()
    @valor_plazo.setter
    def valor_plazo(self, value):
        self.spn_plazo.setValue(value)

    def restablecer_valores(self):
        super().restablecer_valores()
        self.valor_plazo = 0

    