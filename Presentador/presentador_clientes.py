from Vista.gestionar_clientes import GestionarCliente
from Modelo.Cliente import Cliente

class PresentadorCliente:
    def __init__(self, banco):
        self.__banco = banco

#Cargar ventana desde la vista
    def iniciar(self):
        self.__vista = GestionarCliente(self)
        self.cargar_datos()
        self.__vista.show()

    def cargar_datos(self):
        self.__vista.vaciar_tabla()
        for cliente in self.__banco.listaCliente:
            i = self.__vista.tabla.rowCount()
            self.__vista.tabla.insertRow(i)
            self.__vista.agregar_elemento_tabla(i, 0, cliente.nombre)
            self.__vista.agregar_elemento_tabla(i, 1, cliente.sexo)
            self.__vista.agregar_elemento_tabla(i, 2, cliente.ci)
            self.__vista.agregar_elemento_tabla(i, 3, cliente.centro_trabajo)
            self.__vista.agregar_elemento_tabla(i, 4, cliente.ocupacion)
            self.__vista.agregar_elemento_tabla(i, 5, str(cliente.salario))
        self.__vista.tabla.resizeColumnsToContents()

    def rellenar_form_x_tabla(self):
        fila_select = self.__vista.tabla.currentRow()
        if fila_select != -1:
            self.__vista.valor_nombre = self.__vista.tabla.item(fila_select, 0).text()
            self.__vista.valor_sexo = self.__vista.tabla.item(fila_select, 1).text()
            self.__vista.valor_ci = self.__vista.tabla.item(fila_select, 2).text()
            self.__vista.valor_centro_trab = self.__vista.tabla.item(fila_select, 3).text()
            self.__vista.valor_ocup = self.__vista.tabla.item(fila_select, 4).text()
            self.__vista.valor_salario = self.__vista.tabla.item(fila_select, 5).text()

    def insertar_cliente(self):
        try:
            self.__vista.validar_entradas()

            nombre = self.__vista.valor_nombre
            sexo = self.__vista.valor_sexo
            ci = self.__vista.valor_ci
            centro_trab = self.__vista.valor_centro_trab
            ocupacion = self.__vista.valor_ocup
            salario = float(self.__vista.valor_salario)

            cliente = Cliente(nombre, sexo, ci, centro_trab, ocupacion, salario)
            self.__banco.ingresarCliente(cliente)

            self.__vista.restablecer_valores()
            self.cargar_datos()
        except Exception as error:
            self.__vista.mostrar_error(str(error))

    def actualizar_cliente(self):
        try:
            fila_select = self.__vista.tabla.currentRow()
            if fila_select == -1:
                raise Exception("Debe seleccionar un cliente en la tabla para actualizarlo")
            self.__vista.validar_entradas()
            ci_ant = self.__vista.tabla.item(fila_select, 2).text()

            nombre = self.__vista.valor_nombre
            sexo = self.__vista.valor_sexo
            ci = self.__vista.valor_ci
            centro_trab = self.__vista.valor_centro_trab
            ocupacion = self.__vista.valor_ocup
            salario = float(self.__vista.valor_salario)

            cliente = Cliente(nombre, sexo, ci, centro_trab, ocupacion, salario)
            self.__banco.actualizarCliente(ci_ant, cliente)
            self.cargar_datos()
            self.__vista.restablecer_valores()
           

        except Exception as error:
            self.__vista.mostrar_error(str(error))

    def eliminar_cliente(self):
        try:
            fila_select = self.__vista.tabla.currentRow()
            if fila_select == -1:
                raise Exception("Debe seleccionar un cliente en la tabla para eliminarlo")
            else:
                ci = self.__vista.tabla.item(fila_select, 2).text()
                self.__banco.eliminarCliente(ci)
            
            self.cargar_datos()
            self.__vista.restablecer_valores()

        except Exception as error:
            self.__vista.mostrar_error(str(error))
            
    

        

