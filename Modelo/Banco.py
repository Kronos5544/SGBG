from Comercial import Comercial
from Cliente import Cliente
from CuentaSimple import CuentaSimple
<<<<<<< HEAD
from CuentaPF import CuentaPF
from CuentaFF import CuentaFF

class Banco():
    def __init__(self):
        self.__listaCuentaSimple = []
        self.__listaCuentaFF = []
        self.__listaCuentaPF = []
        self.__listaCliente = []
        self.__listaComercial = []


    #Funciones Auxiliares
    def buscarCliente(self, ci):
        for i in range(len(self.__listaCliente)):
            if self.__listaCliente[i].ci == ci:
                return i
        return None
    
    def buscarComercial(self, ci):
        for i in range(len(self.__listaComercial)):
            if self.__listaComercial[i].ci == ci:
                return i
        return None
    
    def actCIClienteCuenta(self, ci_ant, ci_nuevo):
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
        for i in range(len(self.__listaCuentaSimple)):
            if self.__listaCuentaSimple[i].datos_comercial == ci_ant:
                self.__listaCuentaSimple[i].datos_comercial = ci_nuevo
        for i in range(len(self.__listaCuentaPF)):
            if self.__listaCuentaPF[i].datos_comercial == ci_ant:
                self.__listaCuentaPF[i].datos_comercial = ci_nuevo
        for i in range(len(self.__listaCuentaFF)):
            if self.__listaCuentaFF[i].datos_comercial == ci_ant:
                self.__listaCuentaFF[i].datos_comercial = ci_nuevo        

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

    #CRUD: Create, Read, Update, Delete
    
    #Create
    def ingresarCuentaSimple(self, cuenta_simp):
        self.__listaCuentaSimple.append(cuenta_simp)

    def ingresarCuentaFF(self, cuenta_ff):
        self.__listaCuentaFF.append(cuenta_ff)    

    def ingresarCuentaPF(self, cuenta_pf):
        self.__listaCuentaPF.append(cuenta_pf)
       
    def ingresarCliente(self, cliente):
        self.__listaCliente.append(cliente)

    def ingresarComercial(self, comercial):
        self.__listaComercial.append(comercial)

    #Delete
    def eliminarCuentaSimple(self, num):
        self.__listaCuentaSimple = list(filter(lambda x: x.num_cuenta != num, self.__listaCuentaSimple))
    
    def eliminarCuentaFF(self, num):
        self.__listaCuentaFF = list(filter(lambda x: x.num_cuenta != num, self.__listaCuentaFF))

    def eliminarCuentaPF(self, num):
        self.__listaCuentaPF = list(filter(lambda x: x.num_cuenta != num, self.__listaCuentaPF))

    def eliminarCuentaSimple(self, num):
        self.__listaCuentaSimple = list(filter(lambda x: x.num_cuenta != num, self.__listaCuentaSimple))
    
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
    def actualizarCliente(self, ci, cliente):
        indice = self.buscarCliente(ci)
        if indice == None:
            raise Exception("No existe el cliente que desea modificar")
        ind_comp = self.buscarCliente(cliente.ci)
        if(ind_comp == indice):
            self.__listaCliente[indice] = cliente
        elif(ind_comp == None):
            self.actCIClienteCuenta(ci, cliente.ci)
            self.__listaCliente[indice] = cliente
        else:
            raise Exception("El cliente ya existe en el repositorio")
        
    def actualizarComercial(self, ci, comercial):
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
        
    def actualizarCuentaSimple(self, num, cuenta_simp):
        indice = self.buscarCuentaSimple(num)
        if indice == None:
            raise Exception("No existe la cuenta que desea modificar")
        ind_comp = self.buscarCuentaSimple(cuenta_simp.num_cuenta)
        ind_comp2 = self.buscarCuentaPF(cuenta_simp.num_cuenta)
        ind_comp3 = self.buscarCuentaFF(cuenta_simp.num_cuenta)
        if (ind_comp3 != None) or (ind_comp2 != None):
            raise Exception("Ya existe una cuenta de otro tipo con este número")
        elif (ind_comp == indice) or (ind_comp == None):
            self.__listaCuentaSimple[indice] = cuenta_simp
        else:
            raise Exception("La cuenta ya existe en el repositorio")


    def actualizarCuentaPF(self, num, cuenta_pf):
        indice = self.buscarCuentaPF(num)
        if indice == None:
            raise Exception("No existe la cuenta que desea modificar")
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
    def GuardarBDCuentaSimp(self):
        with open('./BD/cuentas_simp.txt', 'w', encoding='utf-8') as fichero:
            contador = len(self.__listaCuentaSimple)
            fichero.write(f"{contador}\n")
            for i in range(contador):
                num_cuenta = self.__listaCuentaSimple[i].num_cuenta
                cliente = self.__listaCuentaSimple[i].cliente
                datos_comercial = self.__listaCuentaSimple[i].datos_comercial
                saldo = str(self.__listaCuentaSimple[i].saldo)
                tipo_moneda = self.__listaCuentaSimple[i].tipo_moneda
                fecha_apertura = str(self.__listaCuentaSimple[i].fecha_apertura)
                fecha_ult_retiro = str(self.__listaCuentaSimple[i].fecha_ult_retiro)

                fichero.write(f"{num_cuenta}, {cliente}, {datos_comercial}, {saldo}, {tipo_moneda}, {fecha_apertura}, {fecha_ult_retiro}\n")

            
    def CargarBDCuentaSimp(self):
        with open('./BD/cuentas_simp.txt', 'r', encoding='utf-8') as fichero:
            contador = int(fichero.readline().strip())
            for i in range(contador):
                lista = fichero.readline().split(", ")
                num_cuenta = lista[0]
                cliente = lista[1]
                datos_comercial = lista[2]
                saldo = float(lista[3])
                tipo_moneda = lista[4]
                fecha_apertura = lista[5]
                fecha_ult_retiro = lista[6].strip()
                cuenta_simp = CuentaSimple(num_cuenta, cliente, datos_comercial, saldo, tipo_moneda, fecha_apertura, fecha_ult_retiro)
                self.__listaCuentaSimple.append(cuenta_simp)


    def GuardarBDCuentaFF(self):
        with open('./BD/cuentas_ff.txt', 'w', encoding='utf-8') as fichero:
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
        with open('./BD/cuentas_ff.txt', 'r', encoding='utf-8') as fichero:
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
        with open('./BD/cuentas_pf.txt', 'w', encoding='utf-8') as fichero:
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
        with open('./BD/cuentas_pf.txt', 'r', encoding='utf-8') as fichero:
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
        with open('./BD/clientes.txt', 'w', encoding='utf-8') as fichero:
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
        with open('./BD/clientes.txt', 'r', encoding='utf-8') as fichero:
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
        with open('./BD/comerciales.txt', 'w', encoding='utf-8') as fichero:
            contador = len(self.__listaComercial)
            fichero.write(f"{contador}\n")
            for i in range(contador):
                nombre = self.__listaComercial[i].nombre
                sexo = self.__listaComercial[i].sexo
                ci = self.__listaComercial[i].ci
                anios_ex = self.__listaComercial[i].anios_ex
                
                fichero.write(f"{nombre}, {sexo}, {ci}, {anios_ex}\n")

    def CargarBDComercial(self):
        with open('./BD/comerciales.txt', 'r', encoding='utf-8') as fichero:
            contador = int(fichero.readline().strip()) 
            for i in range(contador):
                lista = fichero.readline().split(", ")
                nombre = lista[0]
                sexo = lista[1]
                ci = lista[2]
                anios_ex = int(lista[3].strip())
                comercial = Comercial(nombre, sexo, ci, anios_ex)
                self.ingresarComercial(comercial)
=======
from CuentaPF import CuentaPL
from CuentaFF import CuentaFF

class Banco():
    listaCuentaSimple = []
    listaCuantaFF = []
    listaCuentaPF = []
    listaCliente = []
    listaComercial = []
>>>>>>> master
