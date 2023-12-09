from Modelo.Comercial import Comercial
from Modelo.Cliente import Cliente
from Modelo.CuentaSimple import CuentaSimple
from Modelo.CuentaPF import CuentaPF
from Modelo.CuentaFF import CuentaFF
from datetime import date
from copy import deepcopy

class Banco():
    def __init__(self):
        self.__listaCuentaSimple = []
        self.__listaCuentaFF = []
        self.__listaCuentaPF = []
        self.__listaCliente = []
        self.__listaComercial = []


    #Funciones Auxiliares

    def buscarCliente(self, ci):
        #A partir del ci recorro toda la lista de clientes para obtener el índice que tiene en dicha lista y de no encontrarlo devuelvo None
        for i in range(len(self.__listaCliente)):
            if self.__listaCliente[i].ci == ci:
                return i
        return None
    
    def buscarComercial(self, ci):
        #Igual funcionamiento que la función buscarCliente
        for i in range(len(self.__listaComercial)):
            if self.__listaComercial[i].ci == ci:
                return i
        return None
    
    def actCIClienteCuenta(self, ci_ant, ci_nuevo):
        #Esta función se utiliza para cambiar el identificador de cliente de todos los tipos de cuenta, recibiendo el ci a cambiar y el nuevo ci. Se utiliza para cuando se actualiza el ci de un cliente
        #Cada bucle recorre cada lista de cuentas y verifica si el identificador de cliente es el mismo que el parámetro ci_ant y de serlo lo cambia por ci_nuevo
        for i in range(len(self.__listaCuentaSimple)):
            if self.__listaCuentaSimple[i].cliente == ci_ant:
                self.__listaCuentaSimple[i].cliente = ci_nuevo
        for i in range(len(self.__listaCuentaPF)):
            if self.__listaCuentaPF[i].cliente == ci_ant:
                self.__listaCuentaPF[i].cliente = ci_nuevo
        for i in range(len(self.__listaCuentaFF)):
            if self.__listaCuentaFF[i].cliente == ci_ant:
                self.__listaCuentaFF[i].cliente = ci_nuevo 

    def actCIComercialCuenta(self, ci_ant, ci_nuevo):
        #Mismo funcionamiento que la función actCIClienteCuenta pero con el comercial
        for i in range(len(self.__listaCuentaSimple)):
            if self.__listaCuentaSimple[i].datos_comercial == ci_ant:
                self.__listaCuentaSimple[i].datos_comercial = ci_nuevo
        for i in range(len(self.__listaCuentaPF)):
            if self.__listaCuentaPF[i].datos_comercial == ci_ant:
                self.__listaCuentaPF[i].datos_comercial = ci_nuevo
        for i in range(len(self.__listaCuentaFF)):
            if self.__listaCuentaFF[i].datos_comercial == ci_ant:
                self.__listaCuentaFF[i].datos_comercial = ci_nuevo        

    #Las funciones de buscar cuentas reciben como párametro el número de la cuenta a buscar y devuelven el índice que tienen en sus respectivas listas, de no encontrarlos devuelven None
    def buscarCuentaSimple(self, num):
        for i in range(len(self.__listaCuentaSimple)):
            if self.__listaCuentaSimple[i].num_cuenta == num:
                return i
        return None

    def buscarCuentaPF(self, num):
        for i in range(len(self.__listaCuentaPF)):
            if self.__listaCuentaPF[i].num_cuenta == num:
                return i
        return None
    
    def buscarCuentaFF(self, num):
        for i in range(len(self.__listaCuentaFF)):
            if self.__listaCuentaFF[i].num_cuenta == num:
                return i
        return None

    
    #A esta función se le pasa como parámetro el ci a validar e intenta conviertirlo en una fecha con la función date, de no poder conseguirlo devuelve un error
    def validarCI(self, ci):
        try:
            hoy = date.today()
            annio = 1900 + int(ci[0:2]) #Le sumo a los primeros correspondientes al año en el ci 1900 para obtener un año válido sobre el que trabajar
            mes = int(ci[2:4])
            dia = int(ci[4:6])
            if (hoy.year - annio) > 100: #De esta forma calculo la diferencia entre el año actual y el año del ci
                annio += 100 #Esta función solo valida a carnet de personas menores de 100 años así que si la operación anterior da como resultado que la persona tiene más de 100 años se le suma 100 al año para así pasar al sigo 21
            date(annio, mes, dia) #Comprueba que la fecha del ci es una fecha válida, de no serlo devuelve un error
        except Exception:
            raise Exception("El Carnet de identidad es inválido")
        

    #CRUD: Create, Read, Update, Delete
    
    #Create

    #Las funciones de ingresar cuentas, verifican que el cliente y el comercial de la cuenta a ingresar existe en el repositorio, de no existir, lanza un error. Además también comprueban que el número de la cuenta a ingresar no se repita en ninguno de los tipos de cuentas del repositorio
    def ingresarCuentaSimple(self, cuenta_simp): #Comprueba que el cliente existe en el repositorio, de no existir lanza un error
        if self.buscarCliente(cuenta_simp.cliente) == None:
            raise Exception("El cliente no existe, verifique que lo ha ingresado correctamente o cree uno nuevo")
        if self.buscarComercial(cuenta_simp.datos_comercial) == None: #Comrpueba que el comercial existe en el repositorio, de no existir lanza un error
            raise Exception("El comercial no existe, verifique que lo ha ingresado correctamente o cree uno nuevo")
        #Guarda el resultado de buscar el número de cuenta en cada lista existente, si no devuelve None entonces el número ya existen en el repositorio
        ind_comp = self.buscarCuentaSimple(cuenta_simp.num_cuenta)
        ind_comp2 = self.buscarCuentaPF(cuenta_simp.num_cuenta)
        ind_comp3 = self.buscarCuentaFF(cuenta_simp.num_cuenta)

        if (ind_comp != None) or (ind_comp2 != None) or (ind_comp3 != None): #Verifica que no exista ninguna cuenta con el número de cuenta de la nueva cuenta a ingresar, de existir lanza un error
            raise Exception("La cuenta ya existe en el repositorio")
        else:
            self.__listaCuentaSimple.append(cuenta_simp)

    def ingresarCuentaFF(self, cuenta_ff):
        if self.buscarCliente(cuenta_ff.cliente) == None: #Comprueba que el cliente existe en el repositorio, de no existir lanza un error
            raise Exception("El cliente no existe, verifique que lo ha ingresado correctamente o cree uno nuevo")
        if self.buscarComercial(cuenta_ff.datos_comercial) == None: #Comrpueba que el comercial existe en el repositorio, de no existir lanza un error
            raise Exception("El comercial no existe, verifique que lo ha ingresado correctamente o cree uno nuevo")
        #Guarda el resultado de buscar el número de cuenta en cada lista existente, si no devuelve None entonces el número ya existen en el repositorio
        ind_comp2 = self.buscarCuentaSimple(cuenta_ff.num_cuenta)
        ind_comp3 = self.buscarCuentaPF(cuenta_ff.num_cuenta)
        ind_comp = self.buscarCuentaFF(cuenta_ff.num_cuenta)

        if (ind_comp != None) or (ind_comp2 != None) or (ind_comp3 != None): #Verifica que no exista ninguna cuenta con el número de cuenta de la nueva cuenta a ingresar, de existir lanza un error
            raise Exception("La cuenta ya existe en el repositorio")
        else:
            self.__listaCuentaFF.append(cuenta_ff)
    
    def ingresarCuentaPF(self, cuenta_pf):
        if self.buscarCliente(cuenta_pf.cliente) == None: #Comprueba que el cliente existe en el repositorio, de no existir lanza un error
            raise Exception("El cliente no existe, verifique que lo ha ingresado correctamente o cree uno nuevo")
        if self.buscarComercial(cuenta_pf.datos_comercial) == None: #Comrpueba que el comercial existe en el repositorio, de no existir lanza un error
            raise Exception("El comercial no existe, verifique que lo ha ingresado correctamente o cree uno nuevo")
        #Guarda el resultado de buscar el número de cuenta en cada lista existente, si no devuelve None entonces el número ya existen en el repositorio
        ind_comp2 = self.buscarCuentaSimple(cuenta_pf.num_cuenta)
        ind_comp = self.buscarCuentaPF(cuenta_pf.num_cuenta)
        ind_comp3 = self.buscarCuentaFF(cuenta_pf.num_cuenta)

        if (ind_comp != None) or (ind_comp2 != None) or (ind_comp3 != None): #Verifica que no exista ninguna cuenta con el número de cuenta de la nueva cuenta a ingresar, de existir lanza un error
            raise Exception("La cuenta ya existe en el repositorio")
        else:
            self.__listaCuentaPF.append(cuenta_pf)
       
    #Las funciones de ingresar cliente y comercial validan que el ci no se repita en sus respectivas listas y que además sea válido
    def ingresarCliente(self, cliente):
        self.validarCI(cliente.ci)
        ind_comp = self.buscarCliente(cliente.ci)
        if ind_comp == None:
            self.__listaCliente.append(cliente)
        else:
            raise Exception("El cliente ya existe en el repositorio")

    def ingresarComercial(self, comercial):
        self.validarCI(comercial.ci)
        ind_comp = self.buscarComercial(comercial.ci)
        if ind_comp == None:
            self.__listaComercial.append(comercial)
        else:
            raise Exception("El comercial ya existe en el repositorio")

    #Delete

    #Las funciones para eliminar reciben el identificador, en caso de ser una cuenta es el número de cuenta y en el caso de ser un cliente o un comercial es el ci. Luego a través de un filter se sobreescribe su respectiva lista, dejando solo las cuentas, clientes o comerciales que cumplan con el requisito de que su identificador no sea el mismo que el del parámetro
    def eliminarCuentaSimple(self, num):
        self.__listaCuentaSimple = list(filter(lambda x: x.num_cuenta != num, self.__listaCuentaSimple))
    
    def eliminarCuentaFF(self, num):
        self.__listaCuentaFF = list(filter(lambda x: x.num_cuenta != num, self.__listaCuentaFF))

    def eliminarCuentaPF(self, num):
        self.__listaCuentaPF = list(filter(lambda x: x.num_cuenta != num, self.__listaCuentaPF))

    
    #La función eliminar cliente tiene la peculiaridad de eliminar también todas las cuentas que correspondan a dicho cliente
    def eliminarCliente(self, ci):
        self.__listaCliente = list(filter(lambda x: x.ci != ci, self.__listaCliente))
        self.__listaCuentaSimple = list(filter(lambda x: x.cliente != ci, self.__listaCuentaSimple))
        self.__listaCuentaPF = list(filter(lambda x: x.cliente != ci, self.__listaCuentaPF))
        self.__listaCuentaFF = list(filter(lambda x: x.cliente != ci, self.__listaCuentaFF))

    def eliminarComercial(self, ci):
        self.__listaComercial = list(filter(lambda x: x.ci != ci, self.__listaComercial))

    #Read
    @property
    def listaCuentaSimple(self):
        return self.__listaCuentaSimple
    
    @property
    def listaCuentaFF(self):
        return self.__listaCuentaFF
    
    @property
    def listaCuentaPF(self):
        return self.__listaCuentaPF
    
    @property
    def listaCliente(self):
        return self.__listaCliente
    
    @property
    def listaComercial(self):
        return self.__listaComercial
    
    #Update

    #Las funciones de actualizar cliente y comercial reciben el ci del cliente o comercial a modificar y el nuevo cliente o comercial que lo sobreescribirá
    def actualizarCliente(self, ci, cliente):
        self.validarCI(cliente.ci) #Valida el ci del nuevo cliente (Funciones auxiliares)
        indice = self.buscarCliente(ci) #Busca el índice del cliente a modificar por el ci, de no encontrarlo lanza un error
        if indice == None:
            raise Exception("No existe el cliente que desea modificar")
        ind_comp = self.buscarCliente(cliente.ci) #Busca si el ci del nuevo cliente ya existe en el repositorio 
        if(ind_comp == indice): #Si el ci del cliente a modificar y el del nuevo cliente son iguales, entonces quiere decir que no se modificó el atributo ci y entonces el nuevo cliente sobreescribe al anterior
            self.__listaCliente[indice] = cliente
        elif(ind_comp == None): #Si el ci del nuevo cliente no existe en el repositorio entonces quiere decir que se modificará el ci del anterior cliente, por tanto se actualizan los identificadores de todas las cuentas que contenían al anterior cliente con el identificador del nuevo cliente 
            self.actCIClienteCuenta(ci, cliente.ci)
            self.__listaCliente[indice] = cliente #El nuevo cliente sobreescribe al anterior
        else:
            raise Exception("El cliente ya existe en el repositorio") #De existir el ci del nuevo cliente y no ser el mismo que el del anterior, entonces quiere decir que ya existe otro cliente con el ci del nuevo cliente y se lanza un error
        
    def actualizarComercial(self, ci, comercial): #Mismo funcionamiento que la función de actualizar clientes pero con comerciales
        self.validarCI(comercial.ci)
        indice = self.buscarComercial(ci)
        if indice == None:
            raise Exception("No existe el comercial que desea modificar")
        ind_comp = self.buscarComercial(comercial.ci)
        if (ind_comp == indice):
            self.__listaComercial[indice] = comercial
        elif (ind_comp == None):
            self.actCIComercialCuenta(ci, comercial.ci)
            self.__listaComercial[indice] = comercial
        else:
            raise Exception("El comercial ya existe en el repositorio")
        
    #Las funciones de actualizar cuentas reciben como parámetro el número de la cuenta a modificar y la nueva cuenta
    
    def actualizarCuentaSimple(self, num, cuenta_simp):
        indice = self.buscarCuentaSimple(num) #Funciones auxiliares
        if indice == None: #Verifica que la cuenta a modificar existe en el repositorio, de no existir lanza un error
            raise Exception("No existe la cuenta que desea modificar")
        if self.buscarComercial(cuenta_simp.datos_comercial) == None: #Verifica que el comercial existe en el repositorio, de no existir lanza un error
            raise Exception("El comercial no existe, verifique que lo ha ingresado correctamente o cree uno nuevo")
        #Nota: no es necesario comprobar el cliente ya que este no se puede cambiar una vez creada la cuenta
        #Busca si el número de la nueva cuenta se repite en alguna de las listas de cuentas del repositorio
        ind_comp = self.buscarCuentaSimple(cuenta_simp.num_cuenta)
        ind_comp2 = self.buscarCuentaPF(cuenta_simp.num_cuenta)
        ind_comp3 = self.buscarCuentaFF(cuenta_simp.num_cuenta)
        if (ind_comp3 != None) or (ind_comp2 != None): #Comprueba si existe una cuenta de otro tipo con el mismo número que el de la nueva cuenta, de existir lanza un error
            raise Exception("Ya existe una cuenta de otro tipo con este número")
        elif (ind_comp == indice) or (ind_comp == None): #Si el número de la cuenta nueva es el mismo que el de la cuenta anterior o no existe ninguna otra cuenta con el mismo número, se sobreescribe la cuenta anterior con la cuenta nueva
            self.__listaCuentaSimple[indice] = cuenta_simp
        else:
            raise Exception("La cuenta ya existe en el repositorio") #Si existe otra cuenta del mismo tipo con el mismo número que el de la cuenta nueva y no es la cuenta anterior, entonces se lanza un error


    #Las demás funciones de actualizar cuentas tienen el mismo funcionamiente que el de la cuenta simple
    def actualizarCuentaPF(self, num, cuenta_pf):
        indice = self.buscarCuentaPF(num)
        if indice == None:
            raise Exception("No existe la cuenta que desea modificar")
        if self.buscarComercial(cuenta_pf.datos_comercial) == None:
            raise Exception("El comercial no existe, verifique que lo ha ingresado correctamente o cree uno nuevo")
        ind_comp2 = self.buscarCuentaSimple(cuenta_pf.num_cuenta)
        ind_comp = self.buscarCuentaPF(cuenta_pf.num_cuenta)
        ind_comp3 = self.buscarCuentaFF(cuenta_pf.num_cuenta)
        if (ind_comp3 != None) or (ind_comp2 != None):
            raise Exception("Ya existe una cuenta de otro tipo con este número")
        elif (ind_comp == indice) or (ind_comp == None):
            self.__listaCuentaPF[indice] = cuenta_pf
        else:
            raise Exception("La cuenta ya existe en el repositorio")

    def actualizarCuentaFF(self, num, cuenta_ff):
        indice = self.buscarCuentaFF(num)
        if indice == None:
            raise Exception("No existe la cuenta que desea modificar")
        if self.buscarComercial(cuenta_ff.datos_comercial) == None:
            raise Exception("El comercial no existe, verifique que lo ha ingresado correctamente o cree uno nuevo")
        ind_comp2 = self.buscarCuentaSimple(cuenta_ff.num_cuenta)
        ind_comp3 = self.buscarCuentaPF(cuenta_ff.num_cuenta)
        ind_comp = self.buscarCuentaFF(cuenta_ff.num_cuenta)
        if (ind_comp3 != None) or (ind_comp2 != None):
            raise Exception("Ya existe una cuenta de otro tipo con este número")
        elif (ind_comp == indice) or (ind_comp == None):
            self.__listaCuentaFF[indice] = cuenta_ff
        else:
            raise Exception("La cuenta ya existe en el repositorio")


    #Cargar y guardar desde Bases de Datos .txt

    #Las funciones de guardar abren los txt en modo de escritura, lo que elimina todo su contenido y recorren las listas convirtiendo cada atributo en un string, luego escriben todos los atributos del objeto de forma ordenada en una sola línea del txt, una línea para cada objeto de la lista
    #Las funciones de cargar abren los txt en modo de lectura y convierten cada línea en un objeto, convirtiendo cada elemento separado por coma en un atributo, para luego convertirlo en un objeto e ingresarlo en la respectiva lista a la que pertenece
    def GuardarBDCuentaSimp(self):
        with open('./Modelo/BD/cuentas_simp.txt', 'w', encoding='utf-8') as fichero: #Se abre el fichero en modo escritura
            contador = len(self.__listaCuentaSimple) 
            fichero.write(f"{contador}\n") #Estas 2 líneas se usan para guardar el total de elementos de la lista en la primera línea del txt, el \n se usa para hacer un salto de linea en el txt
            for i in range(contador):
                #Se recorre cada objeto de la lista y por cada iteracion se convierten sus atributos a string
                num_cuenta = self.__listaCuentaSimple[i].num_cuenta
                cliente = self.__listaCuentaSimple[i].cliente
                datos_comercial = self.__listaCuentaSimple[i].datos_comercial
                saldo = str(self.__listaCuentaSimple[i].saldo)
                tipo_moneda = self.__listaCuentaSimple[i].tipo_moneda
                fecha_apertura = str(self.__listaCuentaSimple[i].fecha_apertura)
                fecha_ult_retiro = str(self.__listaCuentaSimple[i].fecha_ult_retiro)
                #Se toman sus atributos convertidos en string y se guardan en una sola linea separados cada uno por coma
                fichero.write(f"{num_cuenta}, {cliente}, {datos_comercial}, {saldo}, {tipo_moneda}, {fecha_apertura}, {fecha_ult_retiro}\n") 

            
    def CargarBDCuentaSimp(self):
        self.__listaCuentaSimple = [] #Se vacia la lista a la que se va a realizar la carga para que si se cargan mas de una vez no de errores
        with open('./Modelo/BD/cuentas_simp.txt', 'r', encoding='utf-8') as fichero: #Se abre el fichero en modo lectura
            contador = int(fichero.readline().strip()) #Se guarda la primera linea del fichero que representa el numero total de cuentas en un contador y se le hace .strip() para eliminar los saltos de linea que hace el .txt
            for i in range(contador):
                lista = fichero.readline().split(", ") #Se guarda la linea entera en una lista y se usa split(", ") para separar cada atributo separado por coma como un elemento independiente
                num_cuenta = lista[0]
                cliente = lista[1]
                datos_comercial = lista[2]
                saldo = float(lista[3])
                tipo_moneda = lista[4]
                fecha_apertura = lista[5]
                fecha_ult_retiro = lista[6].strip() #Se usa el .strip en el ultimo elemento para eliminar el salto de linea que se produce en el txt
                #Se crea un objeto del tipo que se desea guardar y se añade a la lista
                cuenta_simp = CuentaSimple(num_cuenta, cliente, datos_comercial, saldo, tipo_moneda, fecha_apertura, fecha_ult_retiro)
                self.__listaCuentaSimple.append(cuenta_simp)


    #Las demás funciones de guardar y cargar funcionan de la misma forma
    def GuardarBDCuentaFF(self):
        with open('./Modelo/BD/cuentas_ff.txt', 'w', encoding='utf-8') as fichero:
            contador = len(self.__listaCuentaFF)
            fichero.write(f"{contador}\n")
            for i in range(contador):
                num_cuenta = self.__listaCuentaFF[i].num_cuenta
                cliente = self.__listaCuentaFF[i].cliente
                datos_comercial = self.__listaCuentaFF[i].datos_comercial
                saldo = str(self.__listaCuentaFF[i].saldo)
                tipo_moneda = self.__listaCuentaFF[i].tipo_moneda
                fecha_apertura = str(self.__listaCuentaFF[i].fecha_apertura)
                fecha_ult_retiro = str(self.__listaCuentaFF[i].fecha_ult_retiro)
                cuota_mensual = str(self.__listaCuentaFF[i].cuota_mensual)

                fichero.write(f"{num_cuenta}, {cliente}, {datos_comercial}, {saldo}, {tipo_moneda}, {fecha_apertura}, {fecha_ult_retiro}, {cuota_mensual}\n")



    def CargarBDCuentaFF(self):
        self.__listaCuentaFF = []
        with open('./Modelo/BD/cuentas_ff.txt', 'r', encoding='utf-8') as fichero:
            contador = int(fichero.readline().strip())
            for i in range(contador):
                lista = fichero.readline().split(", ")
                num_cuenta = lista[0]
                cliente = lista[1]
                datos_comercial = lista[2]
                saldo = float(lista[3])
                tipo_moneda = lista[4]
                fecha_apertura = lista[5]
                fecha_ult_retiro = lista[6]
                cuota_mensual = float(lista[7].strip())
                cuenta_ff = CuentaFF(num_cuenta, cliente, datos_comercial, saldo, tipo_moneda, fecha_apertura, fecha_ult_retiro, cuota_mensual)
                self.__listaCuentaFF.append(cuenta_ff)

    def GuardarBDCuentaPF(self):
        with open('./Modelo/BD/cuentas_pf.txt', 'w', encoding='utf-8') as fichero:
            contador = len(self.__listaCuentaPF)
            fichero.write(f"{contador}\n")
            for i in range(contador):
                num_cuenta = self.__listaCuentaPF[i].num_cuenta
                cliente = self.__listaCuentaPF[i].cliente
                datos_comercial = self.__listaCuentaPF[i].datos_comercial
                saldo = str(self.__listaCuentaPF[i].saldo)
                tipo_moneda = self.__listaCuentaPF[i].tipo_moneda
                fecha_apertura = str(self.__listaCuentaPF[i].fecha_apertura)
                fecha_ult_retiro = str(self.__listaCuentaPF[i].fecha_ult_retiro)
                plazo = str(self.__listaCuentaPF[i].plazo)

                fichero.write(f"{num_cuenta}, {cliente}, {datos_comercial}, {saldo}, {tipo_moneda}, {fecha_apertura}, {fecha_ult_retiro}, {plazo}\n")

    def CargarBDCuentaPF(self):
        self.__listaCuentaPF = []
        with open('./Modelo/BD/cuentas_pf.txt', 'r', encoding='utf-8') as fichero:
            contador = int(fichero.readline().strip())
            for i in range(contador):
                lista = fichero.readline().split(", ")
                num_cuenta = lista[0]
                cliente = lista[1]
                datos_comercial = lista[2]
                saldo = float(lista[3])
                tipo_moneda = lista[4]
                fecha_apertura = lista[5]
                fecha_ult_retiro = lista[6]
                plazo = int(lista[7].strip())
                cuenta_pf = CuentaPF(num_cuenta, cliente, datos_comercial, saldo, tipo_moneda, fecha_apertura, fecha_ult_retiro, plazo)
                self.__listaCuentaPF.append(cuenta_pf)


    def GuardarBDCliente(self):
        with open('./Modelo/BD/clientes.txt', 'w', encoding='utf-8') as fichero:
            contador = len(self.__listaCliente)
            fichero.write(f"{contador}\n")
            for i in range(contador):
                nombre = self.__listaCliente[i].nombre
                sexo = self.__listaCliente[i].sexo
                ci = self.__listaCliente[i].ci
                centro_trabajo = self.__listaCliente[i].centro_trabajo
                ocupacion = self.__listaCliente[i].ocupacion
                salario = str(self.__listaCliente[i].salario)
                
                fichero.write(f"{nombre}, {sexo}, {ci}, {centro_trabajo}, {ocupacion}, {salario}\n")
    
    def CargarBDCliente(self):
        self.__listaCliente = []
        with open('./Modelo/BD/clientes.txt', 'r', encoding='utf-8') as fichero:
            contador = int(fichero.readline().strip()) 
            for i in range(contador):
                lista = fichero.readline().split(", ")
                nombre = lista[0]
                sexo = lista[1]
                ci = lista[2]
                centro_trabajo = lista[3]
                ocupacion = lista[4]
                salario = float(lista[5].strip())
                cliente = Cliente(nombre, sexo, ci, centro_trabajo, ocupacion, salario)
                self.ingresarCliente(cliente)
    
    def GuardarBDComercial(self):
        with open('./Modelo/BD/comerciales.txt', 'w', encoding='utf-8') as fichero:
            contador = len(self.__listaComercial)
            fichero.write(f"{contador}\n")
            for i in range(contador):
                nombre = self.__listaComercial[i].nombre
                sexo = self.__listaComercial[i].sexo
                ci = self.__listaComercial[i].ci
                anios_ex = self.__listaComercial[i].anios_ex
                
                fichero.write(f"{nombre}, {sexo}, {ci}, {anios_ex}\n")

    def CargarBDComercial(self):
        self.__listaComercial = []
        with open('./Modelo/BD/comerciales.txt', 'r', encoding='utf-8') as fichero:
            contador = int(fichero.readline().strip()) 
            for i in range(contador):
                lista = fichero.readline().split(", ")
                nombre = lista[0]
                sexo = lista[1]
                ci = lista[2]
                anios_ex = int(lista[3].strip())
                comercial = Comercial(nombre, sexo, ci, anios_ex)
                self.ingresarComercial(comercial)

    #Funcionalidades
    def calcularInteresxNum(self, num):
        indice = self.buscarCuentaSimple(num)
        indice2 = self.buscarCuentaPF(num)
        indice3 = self.buscarCuentaFF(num)

        if indice != None:
            interes = self.listaCuentaSimple[indice].calcularInteres(), self.listaCuentaSimple[indice].tipo_moneda
        elif indice2 != None:
            interes = self.listaCuentaPF[indice2].calcularInteres(), self.listaCuentaPF[indice2].tipo_moneda
        elif indice3 != None:
            interes = self.listaCuentaFF[indice3].calcularInteres(), self.listaCuentaFF[indice3].tipo_moneda
        else:
            raise Exception("La cuenta no existe en el repositorio")
        
        return interes

    def depositar(self, num, saldo):
        indice = self.buscarCuentaSimple(num)
        indice2 = self.buscarCuentaPF(num)
        indice3 = self.buscarCuentaFF(num)

        if indice != None:
            self.listaCuentaSimple[indice] + saldo
        elif indice2 != None:
            self.listaCuentaPF[indice2] + saldo
        elif indice3 != None:
            self.listaCuentaFF[indice3] + saldo
        else:
            raise Exception("La cuenta no existe en el repositorio")
        
    def retirar(self, num, saldo):
        indice = self.buscarCuentaSimple(num)
        indice2 = self.buscarCuentaPF(num)
        indice3 = self.buscarCuentaFF(num)

        if indice != None:
            if self.listaCuentaSimple[indice].saldo < saldo:
                raise Exception("El monto a retirar no puede ser mayor que el saldo de la cuenta") 
            self.listaCuentaSimple[indice] - saldo

        elif indice2 != None:
            if self.listaCuentaPF[indice2].saldo < saldo:
                raise Exception("El monto a retirar no puede ser mayor que el saldo de la cuenta")
            self.listaCuentaPF[indice2] - saldo
            
        elif indice3 != None:
            if self.listaCuentaFF[indice3].saldo < saldo:
                raise Exception("El monto a retirar no puede ser mayor que el saldo de la cuenta")
            self.listaCuentaFF[indice3] - saldo

        else:
            raise Exception("La cuenta no existe en el repositorio")
        
    def interesPF5Anios(self):
        lista_cuentas = deepcopy(self.listaCuentaPF) #Para crear una nueva lista idéntica a la lista de cuentas pf y trabajar con ella sin afectar a la original
        
        if len(lista_cuentas) == 0:
            raise Exception("No existen Cuentas de PLazo Fijo en el repositorio")
        
        for cuenta in lista_cuentas:
            anio = cuenta.fecha_ult_retiro.year - 5
            cuenta.fecha_ult_retiro = cuenta.fecha_ult_retiro.replace(year = anio).isoformat()
        
        lista = list(map(lambda x : x.calcularInteres(), lista_cuentas))
        return lista
    
    def cuentaMayorSaldo(self):
        lista_cuentas = deepcopy(self.listaCuentaPF) + deepcopy(self.listaCuentaFF) + deepcopy(self.listaCuentaSimple) #Para crear una nueva lista idéntica a la lista de cuentas pf y trabajar con ella sin afectar a la original
        
        if len(lista_cuentas) == 0:
            raise Exception("No existen cuentas en el repositorio")
        
        for cuenta in lista_cuentas:
            cuenta.saldo = cuenta.saldo + cuenta.calcularInteres()
            cuenta.saldo_cup = cuenta.calcularSaldoCup()
        
        lista_cuentas = sorted(lista_cuentas, key = lambda x : x.saldo_cup) #Ordena las cuentas en orden ascendente teniendo en cuenta el saldo_cup

        cliente = self.buscarCliente(lista_cuentas[-1].cliente)

        return cliente, lista_cuentas[-1] #Devuelve una tupla con la cuenta en la última posición (mayor saldo) y su respectivo cliente
    
    def cuentasPFmas10MilCUP(self):
        lista_cuentas_pf_mas_10_mil_pesos = []

        for cuenta in self.listaCuentaPF:

            cuenta.saldo_cup = cuenta.calcularSaldoCup()
            if cuenta.saldo_cup > 10000: #Comprueba que la cuenta tiene más de 10000 y la agrega a la lista de así serlo
                lista_cuentas_pf_mas_10_mil_pesos.append(cuenta)
            else:
                continue

        if len(lista_cuentas_pf_mas_10_mil_pesos) == 0:
            raise Exception("No existen cuentas de Plazo Fijo con más de 10 mil CUP en el repositorio")
        
        lista_cuentas_pf_mas_10_mil_pesos = sorted(lista_cuentas_pf_mas_10_mil_pesos, key = lambda x : x.num_cuenta) #Ordena las cuentas ascendentemente teniendo en cuenta el num_cuenta
        return lista_cuentas_pf_mas_10_mil_pesos #Devuelve una lista de cuentas PF mayores de 10 mil pesos en orden ascendente teniendo en cuenta el numero de cuenta


        



