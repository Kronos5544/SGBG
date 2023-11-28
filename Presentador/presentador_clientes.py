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

    def insertar_cliente(self):
        nombre = self.__vista.valor_nombre
        sexo = self.__vista.valor_sexo
        ci = self.__vista.valor_ci
        centro_trab = self.__vista.valor_centro_trab
        ocupacion = self.__vista.valor_ocup
        salario = self.__vista.valor_salario

        cliente = Cliente(nombre, sexo, ci, centro_trab, ocupacion, salario)
        self.__banco.ingresarCliente(cliente)

        self.cargar_datos()

        

