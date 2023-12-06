from Vista.gestionar_clientes import GestionarCliente
from Modelo.Cliente import Cliente

class PresentadorCliente:
    def __init__(self, banco):
        self.__banco = banco

#Cargar ventana desde la vista
    def iniciar(self):
        self.__vista = GestionarCliente(self)
        self.cargar_datos() #Carga los datos de la tabla antes de iniciar la ventana, para que una vez inicie ya lo haga mostrando los datos
        self.__vista.show() 

#Carga todos los datos en la tabla
    def cargar_datos(self):
        self.__vista.vaciar_tabla() #Una funcion de la vista que vacia todos los datos de la tabla
        for cliente in self.__banco.listaCliente:
            i = self.__vista.tabla.rowCount() #Esta función es similar a un len(), decuelve la cantidad de filas que tiene la tabla
            self.__vista.tabla.insertRow(i) #Esta función crea una nueva fila en la tabla
            #Se agregan los atributos en el orden (fila, columna, string del atributo)
            self.__vista.agregar_elemento_tabla(i, 0, cliente.nombre) 
            self.__vista.agregar_elemento_tabla(i, 1, cliente.sexo)
            self.__vista.agregar_elemento_tabla(i, 2, cliente.ci)
            self.__vista.agregar_elemento_tabla(i, 3, cliente.centro_trabajo)
            self.__vista.agregar_elemento_tabla(i, 4, cliente.ocupacion)
            self.__vista.agregar_elemento_tabla(i, 5, str(cliente.salario))
        self.__vista.tabla.resizeColumnsToContents() #Redimensiona las columnas para ajustarse a los elementos de cada fila

    #Esta función rellena los campos que ingresa el usuario si toca un elemento de la lista
    def rellenar_form_x_tabla(self):
        fila_select = self.__vista.tabla.currentRow() #currentRow() devuelve el elemento de la fila que está siendo seleccionado, si no hay nunguno seleccionado devuelve -1
        if fila_select != -1: 
            self.__vista.valor_nombre = self.__vista.tabla.item(fila_select, 0).text()
            self.__vista.valor_sexo = self.__vista.tabla.item(fila_select, 1).text()
            self.__vista.valor_ci = self.__vista.tabla.item(fila_select, 2).text()
            self.__vista.valor_centro_trab = self.__vista.tabla.item(fila_select, 3).text()
            self.__vista.valor_ocup = self.__vista.tabla.item(fila_select, 4).text()
            self.__vista.valor_salario = self.__vista.tabla.item(fila_select, 5).text()

    #Valida los campos que ingresa el usuario y de ser correctos, crea un objeto con los atributos que ingresa el usuario y lo añade a la lista 
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

            self.__vista.restablecer_valores() #Después de terminar cada operación los campos que rellena el usuario regresan a sus valores predeterminados
            self.cargar_datos() #Después de cada operación se recarga la tabla para que así muestre los cambios efectuados
        except Exception as error:
            self.__vista.mostrar_error(str(error)) #De ocurrir un error, se le muestra al usuario un mensaje de error

    #Actualiza el cliente en la fila seleccionada
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
            self.cargar_datos() #Después de cada operación se recarga la tabla para que así muestre los cambios efectuados 
            self.__vista.restablecer_valores() #Después de terminar cada operación los campos que rellena el usuario regresan a sus valores predeterminados
           

        except Exception as error:
            self.__vista.mostrar_error(str(error)) #De ocurrir un error, se le muestra al usuario un mensaje

#Elimina el cliente en la fila seleccionada
    def eliminar_cliente(self):
        try:
            fila_select = self.__vista.tabla.currentRow()
            if fila_select == -1:
                raise Exception("Debe seleccionar un cliente en la tabla para eliminarlo")
            else:
                ci = self.__vista.tabla.item(fila_select, 2).text()
                self.__banco.eliminarCliente(ci)
            
            self.cargar_datos() #Después de cada operación se recarga la tabla para que así muestre los cambios efectuados
            self.__vista.restablecer_valores() #Después de terminar cada operación los campos que rellena el usuario regresan a sus valores predeterminados

        except Exception as error:
            self.__vista.mostrar_error(str(error)) #De ocurrir un error, se le muestra al usuario un mensaje
            
    

        

