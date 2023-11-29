from Vista.gestionar_cuenta_simp import GestionarCuentaSimple
from Modelo.CuentaSimple import CuentaSimple
from datetime import date

class PresentadorCuentaSimple:
    def __init__(self, banco):
        self.__banco = banco

    def iniciar(self):
        self.__vista = GestionarCuentaSimple(self)
        self.cargar_datos()
        self.__vista.show()
    
    def cargar_datos(self):
        self.__vista.vaciar_tabla()
        for cuenta in self.__banco.listaCuentaSimple:
            i = self.__vista.tabla.rowCount()
            self.__vista.tabla.insertRow(i)
            self.__vista.agregar_elemento_tabla(i, 0, cuenta.num_cuenta)
            self.__vista.agregar_elemento_tabla(i, 1, cuenta.cliente)
            self.__vista.agregar_elemento_tabla(i, 2, cuenta.datos_comercial)
            self.__vista.agregar_elemento_tabla(i, 3, str(cuenta.saldo))
            self.__vista.agregar_elemento_tabla(i, 4, cuenta.tipo_moneda)
            self.__vista.agregar_elemento_tabla(i, 5, cuenta.fecha_apertura.isoformat())
            self.__vista.agregar_elemento_tabla(i, 6, cuenta.fecha_ult_retiro.isoformat())
        self.__vista.tabla.resizeColumnsToContents()

    def rellenar_form_x_tabla(self):
        fila_select = self.__vista.tabla.currentRow()
        if fila_select != -1:
            self.__vista.valor_num_cuenta = self.__vista.tabla.item(fila_select, 0).text()
            self.__vista.valor_cliente = self.__vista.tabla.item(fila_select, 1).text()
            self.__vista.valor_comercial = self.__vista.tabla.item(fila_select, 2).text()
            self.__vista.valor_saldo = self.__vista.tabla.item(fila_select, 3).text()
            self.__vista.valor_tipo_de_moneda = self.__vista.tabla.item(fila_select, 4).text() 
               
    
    def insertar_cuenta_simple(self):
        try:

            self.__vista.validar_entradas()
            num_cuenta = self.__vista.valor_num_cuenta
            cliente = self.__vista.valor_cliente 
            comercial = self.__vista.valor_comercial
            saldo = float(self.__vista.valor_saldo)
            tipo_moneda = self.__vista.valor_tipo_de_moneda
            fecha_apertura = date.today().isoformat()
            fecha_ult_retiro = fecha_apertura

            cuenta_simp = CuentaSimple(num_cuenta, cliente, comercial, saldo, tipo_moneda, fecha_apertura, fecha_ult_retiro)
            self.__banco.ingresarCuentaSimple(cuenta_simp)
            self.cargar_datos()
            self.__vista.restablecer_valores()

        except Exception as error:
            self.__vista.mostrar_error(str(error))

    def actualizar_cuenta_simple(self):
        try:
            fila_select = self.__vista.tabla.currentRow()
            if fila_select == -1:
                raise Exception("Debe seleccionar una cuenta de la tabla para actualizarla")
            else:
                self.__vista.validar_entradas()
                num_anterior = self.__vista.tabla.item(fila_select, 0).text()
                num_cuenta = self.__vista.valor_num_cuenta
                cliente = self.__vista.tabla.item(fila_select, 1).text()
                comercial = self.__vista.valor_comercial
                saldo = float(self.__vista.valor_saldo)
                tipo_moneda = self.__vista.valor_tipo_de_moneda
                fecha_apertura = self.__vista.tabla.item(fila_select, 5).text()
                fecha_ult_retiro = self.__vista.tabla.item(fila_select, 6).text()

                cuenta_simp = CuentaSimple(num_cuenta, cliente, comercial, saldo, tipo_moneda, fecha_apertura, fecha_ult_retiro)
                self.__banco.actualizarCuentaSimple(num_anterior, cuenta_simp)
                self.cargar_datos()
                self.__vista.restablecer_valores()

        except Exception as error:
            self.__vista.mostrar_error(str(error))


    def eliminar_cuenta_simple(self):
        try:
            fila_select = self.__vista.tabla.currentRow()
            if fila_select == -1:
                raise Exception("Debe seleccionar una cuenta de la tabla para eliminarla")
            else:
                num_cuenta = self.__vista.tabla.item(fila_select, 0).text()
                self.__banco.eliminarCuentaSimple(num_cuenta)
                self.cargar_datos()
                self.__vista.restablecer_valores()
            
        except Exception as error:
            self.__vista.mostrar_error(str(error))