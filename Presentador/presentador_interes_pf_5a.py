from Vista.interes_pf_5_anios import InteresPF5Anios
from datetime import date

class PresentadorIntPF5Anios:
    def __init__(self, banco):
        self.__banco = banco

    def iniciar(self):
        self.__vista = InteresPF5Anios(self)
        self.__vista.valor_fecha_creacion = date.today().isoformat()
        self.__vista.show()

    def interes_pf_5_anios(self):
        try:
            lista = self.__banco.interesPF5Anios(self.__vista.valor_fecha_creacion)
            self.__vista.vaciar_tabla() #Una funcion de la vista que vacia todos los datos de la tabla
            for cuenta in lista[1]:
                i = self.__vista.tabla.rowCount() #Esta función es similar a un len(), decuelve la cantidad de filas que tiene la tabla
                self.__vista.tabla.insertRow(i) #Esta función crea una nueva fila en la tabla
                #Se agregan los atributos en el orden (fila, columna, string del atributo)
                self.__vista.agregar_elemento_tabla(i, 0, str(lista[0][i]))
                self.__vista.agregar_elemento_tabla(i, 1, cuenta.num_cuenta)
                self.__vista.agregar_elemento_tabla(i, 2, cuenta.cliente)
                self.__vista.agregar_elemento_tabla(i, 3, cuenta.datos_comercial)
                self.__vista.agregar_elemento_tabla(i, 4, str(cuenta.saldo))
                self.__vista.agregar_elemento_tabla(i, 5, cuenta.tipo_moneda)
                self.__vista.agregar_elemento_tabla(i, 6, cuenta.fecha_apertura.isoformat())
                self.__vista.agregar_elemento_tabla(i, 7, cuenta.fecha_ult_retiro.isoformat())
                self.__vista.agregar_elemento_tabla(i, 8, str(cuenta.plazo))
            self.__vista.tabla.resizeColumnsToContents() #Redimensiona las columnas para ajustarse a los elementos de cada fila
        except Exception as error:
            self.__vista.mostrar_error(str(error))