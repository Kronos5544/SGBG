from Vista.gestionar_comerciales import GestionarComercial
from Modelo.Comercial import Comercial

class PresentadorComercial:
    def __init__(self, banco):
        self.__banco = banco
        

    def iniciar(self):
        self.__vista = GestionarComercial(self)
        self.__vista.show()

    def cargar_datos(self):
        self.__vista.vaciar_tabla()
        for cliente in self.__banco.listaComercial:
            i = self.__vista.tabla.rowCount()
            self.__vista.tabla.insertRow(i)
            self.__vista.agregar_elemento_tabla(i, 0, cliente.nombre)
            self.__vista.agregar_elemento_tabla(i, 1, cliente.sexo)
            self.__vista.agregar_elemento_tabla(i, 2, cliente.ci)
            self.__vista.agregar_elemento_tabla(i, 3, str(cliente.anios_ex))
        self.__vista.tabla.resizeColumnsToContents()

    def rellenar_form_x_tabla(self):
        fila_select = self.__vista.tabla.currentRow()
        if fila_select != -1:
            self.__vista.valor_nombre = self.__vista.tabla.item(fila_select, 0).text()
            self.__vista.valor_sexo = self.__vista.tabla.item(fila_select, 1).text()
            self.__vista.valor_ci = self.__vista.tabla.item(fila_select, 2).text()
            self.__vista.valor_annios_ex = int(self.__vista.tabla.item(fila_select, 3).text())


    def insertar_comercial(self):
        try:
            self.__vista.validar_entradas()

            nombre = self.__vista.valor_nombre
            sexo = self.__vista.valor_sexo
            ci = self.__vista.valor_ci
            anios_ex = self.__vista.valor_annios_ex

            comercial = Comercial(nombre, sexo, ci, anios_ex)
            self.__banco.ingresarComercial(comercial)
            self.cargar_datos()
            self.__vista.restablecer_valores()

        except Exception as error:
            self.__vista.mostrar_error(str(error))

    def actualizar_comercial(self):
        try:
            fila_select = self.__vista.tabla.currentRow()
            if fila_select == -1:
                raise Exception("Debe seleccionar un comercial en la tabla para actualizarlo")
            self.__vista.validar_entradas()
            ci_ant = self.__vista.tabla.item(fila_select, 2).text()

            nombre = self.__vista.valor_nombre
            sexo = self.__vista.valor_sexo
            ci = self.__vista.valor_ci
            anios_ex = self.__vista.valor_annios_ex

            comercial = Comercial(nombre, sexo, ci, anios_ex)
            self.__banco.actualizarComercial(ci_ant, comercial)
            self.cargar_datos()
            self.__vista.restablecer_valores()

        except Exception as error:
            self.__vista.mostrar_error(str(error))

    
    def eliminar_comercial(self):
        try:
            fila_select = self.__vista.tabla.currentRow()
            if fila_select == -1:
                raise Exception("Debe seleccionar un comercial en la tabla para eliminarlo")
            else:
                ci = self.__vista.tabla.item(fila_select, 2).text()
                self.__banco.eliminarComercial(ci)
            
            self.cargar_datos()
            self.__vista.restablecer_valores()

        except Exception as error:
            self.__vista.mostrar_error(str(error))

            

