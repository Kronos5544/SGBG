from Vista.gestionar_comerciales import GestionarComercial
from Modelo.Comercial import Comercial

class PresentadorComercial:
    def __init__(self, banco):
        self.__banco = banco
        

    def iniciar(self):
        self.__vista = GestionarComercial(self)
        self.cargar_datos() #Carga los datos de la tabla antes de iniciar la ventana, para que una vez inicie ya lo haga mostrando los datos
        self.__vista.show()

    def cargar_datos(self):
        self.__vista.vaciar_tabla() #Una funcion de la vista que vacia todos los datos de la tabla
        for comercial in self.__banco.listaComercial:
            i = self.__vista.tabla.rowCount() #Esta función es similar a un len(), decuelve la cantidad de filas que tiene la tabla
            self.__vista.tabla.insertRow(i) #Esta función crea una nueva fila en la tabla
            #Se agregan los atributos en el orden (fila, columna, string del atributo)
            self.__vista.agregar_elemento_tabla(i, 0, comercial.nombre)
            self.__vista.agregar_elemento_tabla(i, 1, comercial.sexo)
            self.__vista.agregar_elemento_tabla(i, 2, comercial.ci)
            self.__vista.agregar_elemento_tabla(i, 3, str(comercial.anios_ex))
        self.__vista.tabla.resizeColumnsToContents() #Redimensiona las columnas para ajustarse a los elementos de cada fila

#Esta función rellena los campos que ingresa el usuario si toca un elemento de la lista
    def rellenar_form_x_tabla(self):
        fila_select = self.__vista.tabla.currentRow()
        if fila_select != -1:
            self.__vista.valor_nombre = self.__vista.tabla.item(fila_select, 0).text()
            self.__vista.valor_sexo = self.__vista.tabla.item(fila_select, 1).text()
            self.__vista.valor_ci = self.__vista.tabla.item(fila_select, 2).text()
            self.__vista.valor_annios_ex = int(self.__vista.tabla.item(fila_select, 3).text())


  #Valida los campos que ingresa el usuario y de ser correctos, crea un objeto con los atributos que ingresa el usuario y lo añade a la lista 
    def insertar_comercial(self):
        try:
            self.__vista.validar_entradas()

            nombre = self.__vista.valor_nombre
            sexo = self.__vista.valor_sexo
            ci = self.__vista.valor_ci
            anios_ex = self.__vista.valor_annios_ex

            comercial = Comercial(nombre, sexo, ci, anios_ex)
            self.__banco.ingresarComercial(comercial)
            self.cargar_datos() #Después de cada operación se recarga la tabla para que así muestre los cambios efectuados
            self.__vista.restablecer_valores() #Después de terminar cada operación los campos que rellena el usuario regresan a sus valores predeterminados

        except Exception as error:
            self.__vista.mostrar_error(str(error)) #De ocurrir un error, se le muestra al usuario un mensaje de error

 #Actualiza el comercial en la fila seleccionada
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
            self.cargar_datos() #Después de cada operación se recarga la tabla para que así muestre los cambios efectuados
            self.__vista.restablecer_valores() #Después de terminar cada operación los campos que rellena el usuario regresan a sus valores predeterminados

        except Exception as error:
            self.__vista.mostrar_error(str(error)) #De ocurrir un error, se le muestra al usuario un mensaje de error

    #Elimina el comercial en la fila seleccionada
    def eliminar_comercial(self):
        try:
            fila_select = self.__vista.tabla.currentRow()
            if fila_select == -1:
                raise Exception("Debe seleccionar un comercial en la tabla para eliminarlo")
            else:
                ci = self.__vista.tabla.item(fila_select, 2).text()
                self.__banco.eliminarComercial(ci)
            
            self.cargar_datos() #Después de cada operación se recarga la tabla para que así muestre los cambios efectuados
            self.__vista.restablecer_valores() #Después de terminar cada operación los campos que rellena el usuario regresan a sus valores predeterminados

        except Exception as error:
            self.__vista.mostrar_error(str(error)) #De ocurrir un error, se le muestra al usuario un mensaje de error

            

