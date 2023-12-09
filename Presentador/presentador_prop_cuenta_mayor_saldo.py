from Vista.prop_cuenta_mayor_saldo import PropCuentaMayorSaldo

class PresentadorPropCuentaMayorSaldo:
    def __init__(self, banco):
        self.__banco = banco

    def iniciar(self):
        self.__vista = PropCuentaMayorSaldo(self)
        self.prop_cuenta_may_saldo()
        self.__vista.show()

    def prop_cuenta_may_saldo(self):
        try:
            datos = self.__banco.cuentaMayorSaldo()
            self.__vista.vaciar_tabla() #Una funcion de la vista que vacia todos los datos de la tabla
            i = self.__vista.tabla.rowCount() #Esta función es similar a un len(), decuelve la cantidad de filas que tiene la tabla
            self.__vista.tabla.insertRow(i) #Esta función crea una nueva fila en la tabla
            #Se agregan los atributos en el orden (fila, columna, string del atributo)
            self.__vista.agregar_elemento_tabla(i, 0, datos[0].nombre) 
            self.__vista.agregar_elemento_tabla(i, 1, datos[0].sexo)
            self.__vista.agregar_elemento_tabla(i, 2, datos[0].ci)
            self.__vista.agregar_elemento_tabla(i, 3, datos[0].centro_trabajo)
            self.__vista.agregar_elemento_tabla(i, 4, datos[0].ocupacion)
            self.__vista.agregar_elemento_tabla(i, 5, str(datos[0].salario))
            self.__vista.agregar_elemento_tabla(i, 6, datos[1].num_cuenta)
            self.__vista.agregar_elemento_tabla(i, 7, str(datos[1].saldo))
            self.__vista.agregar_elemento_tabla(i, 8, datos[1].tipo_moneda)
            self.__vista.tabla.resizeColumnsToContents() #Redimensiona las columnas para ajustarse a los elementos de cada fila
        except Exception as error:
            self.__vista.mostrar_error(str(error))