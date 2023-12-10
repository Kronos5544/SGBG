import unittest
from Modelo.Banco import Banco
from Modelo.Cliente import Cliente
from Modelo.Comercial import Comercial
from Modelo.CuentaSimple import CuentaSimple
from Modelo.CuentaFF import CuentaFF
from Modelo.CuentaPF import CuentaPF

class TestBanco(unittest.TestCase):
    def setUp(self):
        self.banco = Banco()

        self.cliente = Cliente("Pepe Antonio", "M", "03031976450", "Paquito Gonzales", "Gerente", 5000.00)
        self.cliente2 = Cliente("Laura Maria", "F", "03031976450", "Paquito Gonzales", "Secretaria", 2500.00)

        self.comercial = Comercial("Juan Almeida", "M", "03031976400", 5)
        self.comercial2 = Comercial("Juan Perez", "M", "03031976400", 2)

        self.cuenta_ff = CuentaFF("0325469887421245", "03031976450", "03031976400", 8000.00, "CUP", "2021-05-28", "2022-03-25", 200.00)
        self.cuenta_ff2 = CuentaFF("0325469887421245", "03031976450", "03031976400", 7000.00, "CUP", "2021-05-28", "2022-03-25", 100.00)
        
        self.cuenta_simp = CuentaSimple("0325469887421246", "03031976450", "03031976400", 8000.00, "CUP", "2021-05-28", "2022-03-25")
        self.cuenta_simp2 = CuentaSimple("0325469887421246", "03031976450", "03031976400", 6000.00, "EUR", "2021-05-28", "2022-03-25")
        
        self.cuenta_pf = CuentaPF("0325469887421247", "03031976450", "03031976400", 8000.00, "CUP", "2021-05-28", "2022-03-25", 1)
        self.cuenta_pf2 = CuentaPF("0325469887421247", "03031976450", "03031976400", 2800.00, "CUP", "2021-05-28", "2022-03-25", 5)


    def test_property(self):
        self.assertEqual(self.banco.listaCliente, [])
        self.assertEqual(self.banco.listaComercial, [])
        self.assertEqual(self.banco.listaCuentaFF, [])
        self.assertEqual(self.banco.listaCuentaPF, [])
        self.assertEqual(self.banco.listaCuentaSimple, [])

    
    def test_ingresar(self):
        self.assertEqual(len(self.banco.listaCliente), 0)
        self.banco.ingresarCliente(self.cliente)
        self.assertEqual(len(self.banco.listaCliente), 1)

        self.assertEqual(len(self.banco.listaComercial), 0)
        self.banco.ingresarComercial(self.comercial)
        self.assertEqual(len(self.banco.listaComercial), 1)
        self.banco.ingresarCuentaSimple(self.cuenta_simp)
        self.assertEqual(len(self.banco.listaCuentaSimple), 1)

        self.assertEqual(len(self.banco.listaCuentaFF), 0)
        self.banco.ingresarCuentaFF(self.cuenta_ff)
        self.assertEqual(len(self.banco.listaCuentaFF), 1)

        self.assertEqual(len(self.banco.listaCuentaPF), 0)
        self.banco.ingresarCuentaPF(self.cuenta_pf)
        self.assertEqual(len(self.banco.listaCuentaPF), 1)

        #Comprobando si no deja ingresar cuentas y clientes con el mismo numero o ci
        with self.assertRaises(Exception):
            self.banco.ingresarCliente(self.cliente2)
            
        with self.assertRaises(Exception):    
            self.banco.ingresarComercial(self.comercial2)

        with self.assertRaises(Exception):    
            self.banco.ingresarCuentaSimple(self.cuenta_simp2)
        
        with self.assertRaises(Exception):    
            self.banco.ingresarCuentaFF(self.cuenta_ff2)
        
        with self.assertRaises(Exception):    
            self.banco.ingresarCuentaPF(self.cuenta_ff2)

        #Probando que no deja ingresar cuentas con ci que no existen en el repositorio
        self.cuenta_simp2.cliente = "03031978900"  #Se cambia el cliente para que no exista en el repositorio
        self.cuenta_simp2.num_cuenta = "5478963256879547" #Se arregla el número de cuenta para que no de error

        with self.assertRaises(Exception): #Da ok si la función lanza un error    
            self.banco.ingresarCuentaSimple(self.cuenta_simp2)

        self.cuenta_simp2.datos_comercial = "03031978901" #Se cambia el comercial para comprobar si da error
        self.cuenta_simp2.cliente = "03031976450" #Se arregla el cliente para que no de error

        with self.assertRaises(Exception): #Da ok si la función lanza un error    
            self.banco.ingresarCuentaSimple(self.cuenta_simp2)



        self.cuenta_ff2.cliente = "03031978900" #Se cambia el cliente para que no exista en el repositorio
        self.cuenta_ff2.num_cuenta = "5478963256879547" #Se arregla el número de cuenta para que no de error
        
        with self.assertRaises(Exception): #Da ok si la función lanza un error    
            self.banco.ingresarCuentaFF(self.cuenta_ff2)

        self.cuenta_ff2.datos_comercial = "03031978901" #Se cambia el comercial para comprobar si da error
        self.cuenta_ff2.cliente = "03031976450" #Se arregla el cliente para que no de error

        with self.assertRaises(Exception): #Da ok si la función lanza un error    
            self.banco.ingresarCuentaFF(self.cuenta_ff2)
        


        self.cuenta_pf2.cliente = "03031978900" #Se cambia el cliente para que no exista en el repositorio
        self.cuenta_pf2.num_cuenta = "5478963256879547" #Se arregla el número de cuenta para que no de error
        
        with self.assertRaises(Exception): #Da ok si la función lanza un error    
            self.banco.ingresarCuentaPF(self.cuenta_pf2)

        self.cuenta_pf2.datos_comercial = "03031978901" #Se cambia el comercial para comprobar si da error
        self.cuenta_pf2.cliente = "03031976450" #Se arregla el cliente para que no de error

        with self.assertRaises(Exception): #Da ok si la función lanza un error    
            self.banco.ingresarCuentaPF(self.cuenta_pf2)
    
    def test_eliminar(self):
        self.banco.ingresarCliente(self.cliente)
        self.banco.ingresarComercial(self.comercial)
        self.banco.ingresarCuentaSimple(self.cuenta_simp)
        self.banco.ingresarCuentaFF(self.cuenta_ff)
        self.banco.ingresarCuentaPF(self.cuenta_pf)

        #El cliente también elimina las cuentas asociadas
        self.assertEqual(len(self.banco.listaCliente), 1)
        self.assertEqual(len(self.banco.listaCuentaSimple), 1)
        self.assertEqual(len(self.banco.listaCuentaPF), 1)
        self.assertEqual(len(self.banco.listaCuentaFF), 1)
        self.banco.eliminarCliente(self.cliente.ci)
        self.assertEqual(len(self.banco.listaCuentaSimple), 0)
        self.assertEqual(len(self.banco.listaCuentaPF), 0)
        self.assertEqual(len(self.banco.listaCuentaFF), 0)
        self.assertEqual(len(self.banco.listaCliente), 0)

        self.assertEqual(len(self.banco.listaComercial), 1)
        self.banco.eliminarComercial(self.comercial.ci)
        self.assertEqual(len(self.banco.listaComercial), 0)

        #Reingresando los datos para comprobar la eliminación de cuentas
        self.banco.ingresarCliente(self.cliente)
        self.banco.ingresarComercial(self.comercial)
        self.banco.ingresarCuentaSimple(self.cuenta_simp)
        self.banco.ingresarCuentaFF(self.cuenta_ff)
        self.banco.ingresarCuentaPF(self.cuenta_pf)


        self.assertEqual(len(self.banco.listaCuentaSimple), 1)
        self.banco.eliminarCuentaSimple(self.cuenta_simp.num_cuenta)
        self.assertEqual(len(self.banco.listaCuentaSimple), 0)

        self.assertEqual(len(self.banco.listaCuentaFF), 1)
        self.banco.eliminarCuentaFF(self.cuenta_ff.num_cuenta)
        self.assertEqual(len(self.banco.listaCuentaFF), 0)

        self.assertEqual(len(self.banco.listaCuentaPF), 1)
        self.banco.eliminarCuentaPF(self.cuenta_pf.num_cuenta)
        self.assertEqual(len(self.banco.listaCuentaPF), 0)

    def test_actualizar(self):
        self.banco.ingresarCliente(self.cliente)
        self.banco.ingresarComercial(self.comercial)
        self.banco.ingresarCuentaSimple(self.cuenta_simp)
        self.banco.ingresarCuentaFF(self.cuenta_ff)
        self.banco.ingresarCuentaPF(self.cuenta_pf)

        #Comprobando si se actualiza correctamente
        self.assertEqual(self.banco.listaCliente[0].nombre, "Pepe Antonio")
        self.banco.actualizarCliente(self.cliente.ci, self.cliente2)
        self.assertEqual(self.banco.listaCliente[0].nombre, "Laura Maria")

        self.assertEqual(self.banco.listaComercial[0].nombre, "Juan Almeida")
        self.banco.actualizarComercial(self.comercial.ci, self.comercial2)
        self.assertEqual(self.banco.listaComercial[0].nombre, "Juan Perez")

        self.assertEqual(self.banco.listaCuentaSimple[0].saldo, 8000.00)
        self.banco.actualizarCuentaSimple(self.cuenta_simp.num_cuenta, self.cuenta_simp2)
        self.assertEqual(self.banco.listaCuentaSimple[0].saldo, 6000.00)

        self.assertEqual(self.banco.listaCuentaPF[0].saldo, 8000.00)
        self.banco.actualizarCuentaPF(self.cuenta_pf.num_cuenta, self.cuenta_pf2)
        self.assertEqual(self.banco.listaCuentaPF[0].saldo, 2800.00)

        self.assertEqual(self.banco.listaCuentaFF[0].saldo, 8000.00)
        self.banco.actualizarCuentaFF(self.cuenta_ff.num_cuenta, self.cuenta_ff2)
        self.assertEqual(self.banco.listaCuentaFF[0].saldo, 7000.00)


        

        #Comprobando si se lanza error al intentar actualizar una cuenta cuyo numero ya existe en una cuenta de otro tipo
        self.cuenta_simp.num_cuenta = self.cuenta_pf2.num_cuenta
        with self.assertRaises(Exception):
            self.banco.actualizarCuentaSimple(self.cuenta_simp2.num_cuenta, self.cuenta_simp)
        self.cuenta_pf.num_cuenta = self.cuenta_ff2.num_cuenta
        with self.assertRaises(Exception):
            self.banco.actualizarCuentaPF(self.cuenta_pf2.num_cuenta, self.cuenta_pf)
        self.cuenta_ff.num_cuenta = self.cuenta_simp2.num_cuenta
        with self.assertRaises(Exception):    
            self.banco.actualizarCuentaFF(self.cuenta_ff2.num_cuenta, self.cuenta_ff)


        
        #Cambiando valores para poder ingresar clientes, comerciales y cuentas nuevas
        self.cliente.ci = "03031976850"
        self.comercial.ci = "0303197550"
        self.cuenta_simp.num_cuenta = "0325469887421258"
        self.cuenta_pf.num_cuenta = "0325469887421259"
        self.cuenta_ff.num_cuenta = "0325469887421264"

        #Ingresando nuevos clientes, cuentas y comerciales
        self.banco.ingresarCliente(self.cliente)
        self.banco.ingresarComercial(self.comercial)
        self.banco.ingresarCuentaSimple(self.cuenta_simp)
        self.banco.ingresarCuentaFF(self.cuenta_ff)
        self.banco.ingresarCuentaPF(self.cuenta_pf)

        #Comprobando que se lanza un error si los ci o num_cuenta no existen en el repositorio
        with self.assertRaises(Exception):
            self.banco.actualizarCliente("03031976554", self.cliente)
        with self.assertRaises(Exception):
            self.banco.actualizarComercial("03031976554", self.comercial)
        with self.assertRaises(Exception):
            self.banco.actualizarCuentaSimple("3164579581346795", self.cuenta_simp)
        with self.assertRaises(Exception):
            self.banco.actualizarCuentaPF("3164579581346795", self.cuenta_pf)
        with self.assertRaises(Exception):    
            self.banco.actualizarCuentaFF("3164579581346795", self.cuenta_ff)

        #Comprobando si se lanza un error si se pasa un cliente, comercial o cuenta que ya existe en el repositorio
        with self.assertRaises(Exception):
            self.banco.actualizarCliente(self.cliente2.ci, self.cliente)
        with self.assertRaises(Exception):
            self.banco.actualizarComercial(self.comercial2.ci, self.comercial)
        with self.assertRaises(Exception):
            self.banco.actualizarCuentaSimple(self.cuenta_simp2.num_cuenta, self.cuenta_simp)
        with self.assertRaises(Exception):
            self.banco.actualizarCuentaPF(self.cuenta_pf.num_cuenta, self.cuenta_pf2)
        with self.assertRaises(Exception):    
            self.banco.actualizarCuentaFF(self.cuenta_ff.num_cuenta, self.cuenta_ff2)

    def test_guardar_cargar_BD(self):
        #Vaciando los archivos de texto
        self.banco.GuardarBDComercial()
        self.banco.GuardarBDCliente()
        self.banco.GuardarBDCuentaSimp()
        self.banco.GuardarBDCuentaPF()
        self.banco.GuardarBDCuentaFF()
        
        #Ingresando un objeto a cada lista
        self.banco.ingresarCliente(self.cliente)
        self.banco.ingresarComercial(self.comercial)
        self.banco.ingresarCuentaSimple(self.cuenta_simp)
        self.banco.ingresarCuentaFF(self.cuenta_ff)
        self.banco.ingresarCuentaPF(self.cuenta_pf)
        
        #Guardando las listas en los txt
        self.banco.GuardarBDComercial()
        self.banco.GuardarBDCliente()
        self.banco.GuardarBDCuentaSimp()
        self.banco.GuardarBDCuentaPF()
        self.banco.GuardarBDCuentaFF()

        #Eliminando los elementos de las listas
        self.banco.eliminarCliente(self.cliente.ci)
        self.banco.eliminarComercial(self.comercial.ci)
        self.banco.eliminarCuentaSimple(self.cuenta_simp.num_cuenta)
        self.banco.eliminarCuentaPF(self.cuenta_pf.num_cuenta)
        self.banco.eliminarCuentaFF(self.cuenta_ff.num_cuenta)

        #Comprobando que las listas esten vacias luego de la eliminacion
        self.assertEqual(len(self.banco.listaCliente), 0)
        self.assertEqual(len(self.banco.listaComercial), 0)
        self.assertEqual(len(self.banco.listaComercial), 0)
        self.assertEqual(len(self.banco.listaComercial), 0)
        self.assertEqual(len(self.banco.listaComercial), 0)

        #Cargando la BD
        self.banco.CargarBDComercial()
        self.banco.CargarBDCliente()
        self.banco.CargarBDCuentaSimp()
        self.banco.CargarBDCuentaPF()
        self.banco.CargarBDCuentaFF()

        #Comprobando que se cargó correctamente
        self.assertEqual(len(self.banco.listaCliente), 1)
        self.assertEqual(len(self.banco.listaComercial), 1)
        self.assertEqual(len(self.banco.listaComercial), 1)
        self.assertEqual(len(self.banco.listaComercial), 1)
        self.assertEqual(len(self.banco.listaComercial), 1)

        #Restaurando BD
        self.banco.eliminarCliente(self.cliente.ci)
        self.banco.eliminarComercial(self.comercial.ci)
        self.banco.eliminarCuentaSimple(self.cuenta_simp.num_cuenta)
        self.banco.eliminarCuentaPF(self.cuenta_pf.num_cuenta)
        self.banco.eliminarCuentaFF(self.cuenta_ff.num_cuenta)

        self.banco.GuardarBDComercial()
        self.banco.GuardarBDCliente()
        self.banco.GuardarBDCuentaSimp()
        self.banco.GuardarBDCuentaPF()
        self.banco.GuardarBDCuentaFF()

    def test_func_auxiliares(self):        
        self.banco.ingresarCliente(self.cliente)
        self.banco.ingresarComercial(self.comercial)
        self.banco.ingresarCuentaSimple(self.cuenta_simp)
        self.banco.ingresarCuentaFF(self.cuenta_ff)
        self.banco.ingresarCuentaPF(self.cuenta_pf)

        #Probando funciones de busqueda
        self.assertEqual(self.banco.buscarCliente(self.cliente.ci), 0)
        self.assertEqual(self.banco.buscarCliente("03031975480"), None)
        
        self.assertEqual(self.banco.buscarComercial(self.comercial.ci), 0)
        self.assertEqual(self.banco.buscarCliente("03031975480"), None)

        self.assertEqual(self.banco.buscarCuentaSimple(self.cuenta_simp.num_cuenta), 0)
        self.assertEqual(self.banco.buscarCuentaSimple("552151123180154"), None)

        self.assertEqual(self.banco.buscarCuentaPF(self.cuenta_pf.num_cuenta), 0)
        self.assertEqual(self.banco.buscarCuentaPF("552151123180154"), None)

        self.assertEqual(self.banco.buscarCuentaFF(self.cuenta_ff.num_cuenta), 0)
        self.assertEqual(self.banco.buscarCuentaFF("552151123180154"), None)

        #Probando funcion validarCI()
        self.assertEqual(self.banco.validarCI('03031976401'), None)

        with self.assertRaises(Exception):
            self.banco.validarCI('03251976401')

        with self.assertRaises(Exception):
            self.banco.validarCI('03034876401')

        #Probando funciones de actualizar CI de comerciales y clientes en cuentas
        self.assertEqual(self.banco.listaCuentaSimple[0].cliente, self.cliente.ci)
        self.assertEqual(self.banco.listaCuentaPF[0].cliente, self.cliente.ci)
        self.assertEqual(self.banco.listaCuentaFF[0].cliente, self.cliente.ci)

        self.assertEqual(self.banco.listaCuentaSimple[0].datos_comercial, self.comercial.ci)
        self.assertEqual(self.banco.listaCuentaPF[0].datos_comercial, self.comercial.ci)
        self.assertEqual(self.banco.listaCuentaFF[0].datos_comercial, self.comercial.ci)

        self.banco.actCIClienteCuenta(self.cliente.ci, '03031976401')
        self.banco.actCIComercialCuenta(self.comercial.ci, '03031976402')

        self.assertEqual(self.banco.listaCuentaSimple[0].cliente, '03031976401')
        self.assertEqual(self.banco.listaCuentaPF[0].cliente, '03031976401')
        self.assertEqual(self.banco.listaCuentaFF[0].cliente, '03031976401')

        self.assertEqual(self.banco.listaCuentaSimple[0].datos_comercial, '03031976402')
        self.assertEqual(self.banco.listaCuentaPF[0].datos_comercial, '03031976402')
        self.assertEqual(self.banco.listaCuentaFF[0].datos_comercial, '03031976402')
    
    def test_calcular_interes_x_num(self):
        self.banco.ingresarCliente(self.cliente)
        self.banco.ingresarComercial(self.comercial)
        self.banco.ingresarCuentaSimple(self.cuenta_simp)
        self.banco.ingresarCuentaFF(self.cuenta_ff)
        self.banco.ingresarCuentaPF(self.cuenta_pf)

        self.assertEqual(self.banco.calcularInteresxNum(self.cuenta_simp.num_cuenta), (320, "CUP"))
        self.assertEqual(self.banco.calcularInteresxNum(self.cuenta_pf.num_cuenta), (640, "CUP"))
        self.assertEqual(self.banco.calcularInteresxNum(self.cuenta_ff.num_cuenta), (480, "CUP"))
        
    def test_depositar(self):
        self.banco.ingresarCliente(self.cliente)
        self.banco.ingresarComercial(self.comercial)
        self.banco.ingresarCuentaSimple(self.cuenta_simp)
        self.banco.ingresarCuentaFF(self.cuenta_ff)
        self.banco.ingresarCuentaPF(self.cuenta_pf)

        #Probando depositar en cuenta simple
        self.assertEqual(self.banco.listaCuentaSimple[0].saldo, 8000.00)
        self.banco.depositar(self.cuenta_simp.num_cuenta, 500.00)
        calc_manual = 8000 + round(8000.00 * 0.04, 2) + 500 #Calculando interes y suma manualmente
        self.assertEqual(self.banco.listaCuentaSimple[0].saldo, calc_manual)

        #Probando depositar en cuenta plazo fijo
        self.assertEqual(self.banco.listaCuentaPF[0].saldo, 8000.00)
        self.banco.depositar(self.cuenta_pf.num_cuenta, 800.00)
        self.assertEqual(self.banco.listaCuentaPF[0].saldo, 8800.00)

        #Probando depositar en cuenta formación de fondos
        self.assertEqual(self.banco.listaCuentaFF[0].saldo, 8000.00)
        self.banco.depositar(self.cuenta_ff.num_cuenta, 750.00)
        calc_manual = 8000 + round(8000.00 * 0.06, 2) + 750 #Calculando interes y suma manualmente
        self.assertEqual(self.banco.listaCuentaFF[0].saldo, calc_manual)

        #Probando que lanza error al no encontrar la cuenta
        with self.assertRaises(Exception):
            self.banco.depositar("254569885454215", 800)

    def test_retirar(self):
        self.banco.ingresarCliente(self.cliente)
        self.banco.ingresarComercial(self.comercial)
        self.banco.ingresarCuentaSimple(self.cuenta_simp)
        self.banco.ingresarCuentaFF(self.cuenta_ff)
        self.banco.ingresarCuentaPF(self.cuenta_pf)

        #Probando retirar en cuenta simple
        self.assertEqual(self.banco.listaCuentaSimple[0].saldo, 8000.00)
        self.banco.retirar(self.cuenta_simp.num_cuenta, 500.00)
        calc_manual = 8000 + round(8000.00 * 0.04, 2) - 500 #Calculando interes y resta manualmente
        self.assertEqual(self.banco.listaCuentaSimple[0].saldo, calc_manual)
        with self.assertRaises(Exception):
            self.banco.retirar(self.cuenta_simp.num_cuenta, 70000)
       

        #Probando retirar en cuenta formacion de fondos
        self.assertEqual(self.banco.listaCuentaFF[0].saldo, 8000.00)
        self.banco.retirar(self.cuenta_ff.num_cuenta, 700.00)
        calc_manual = 8000 + round(8000.00 * 0.06, 2) - 700 #Calculando interes y resta manualmente
        self.assertEqual(self.banco.listaCuentaFF[0].saldo, calc_manual)

        with self.assertRaises(Exception):      
            self.banco.retirar(self.cuenta_ff.num_cuenta, 80000)

        #Probando retirar en cuenta de Plazo Fijo
        self.assertEqual(self.banco.listaCuentaPF[0].saldo, 8000.00)
        self.banco.retirar(self.cuenta_pf.num_cuenta, 900.00)
        calc_manual = 8000 + round(8000.00 * 0.08, 2) - 900 #Calculando interes y resta manualmente
        self.assertEqual(self.banco.listaCuentaPF[0].saldo, calc_manual)
        with self.assertRaises(Exception):
            self.banco.retirar(self.cuenta_pf.num_cuenta, 40000)

        #Probando que lanza error al no encontrar la cuenta
        with self.assertRaises(Exception):
            self.banco.retirar("254569885454215", 800)


    def test_interes_cuenta_pf_en_5_anios(self):
        #Manda un error si no hay cuentas pf en el banco
        with self.assertRaises(Exception):
            self.banco.interesPF5Anios("2021-05-28")

        self.banco.ingresarCliente(self.cliente)
        self.banco.ingresarComercial(self.comercial)
        self.banco.ingresarCuentaSimple(self.cuenta_simp)
        self.banco.ingresarCuentaFF(self.cuenta_ff)
        self.banco.ingresarCuentaPF(self.cuenta_pf)

        self.cuenta_pf2.num_cuenta = "032564785412365478"
        self.banco.ingresarCuentaPF(self.cuenta_pf2)
        
        self.assertEqual(self.banco.interesPF5Anios("2021-05-28")[0], [8000 * 0.08 * 1, 2800 * 0.16 * 5])

        with self.assertRaises(Exception):
            self.banco.interesPF5Anios("2022-05-14")


    def test_cuenta_mayor_saldo(self):

        with self.assertRaises(Exception): #Comprobando que manda error si no existen cuentas en el repositorio
            self.banco.cuentaMayorSaldo()

        self.banco.ingresarCliente(self.cliente)
        self.banco.ingresarComercial(self.comercial)
        self.banco.ingresarCuentaSimple(self.cuenta_simp)
        self.banco.ingresarCuentaFF(self.cuenta_ff)
        self.banco.ingresarCuentaPF(self.cuenta_pf)
        
        self.cuenta_ff.tipo_moneda = "CUC" #Como todas las cuentas tienen el mismo saldo y en CUP, cambio una a CUC para que sea la de mayor saldo
        self.assertEqual(self.banco.cuentaMayorSaldo()[1].num_cuenta, self.cuenta_ff.num_cuenta) #Comparo si la cuenta retornada es la misma que la cuenta esperada a través del número de cuenta

        self.cuenta_simp.tipo_moneda = "USD" #Cambio la cuenta simple a USD para que sea la de mayor saldo
        self.assertEqual(self.banco.cuentaMayorSaldo()[1].num_cuenta, self.cuenta_simp.num_cuenta) #Comparo si la cuenta retornada es la misma que la cuenta esperada a través del número de cuenta

        self.cuenta_pf.tipo_moneda = "EUR" #Cambio la cuenta pf a EUR para que sea la de mayor saldo
        self.assertEqual(self.banco.cuentaMayorSaldo()[1].num_cuenta, self.cuenta_pf.num_cuenta) #Comparo si la cuenta retornada es la misma que la cuenta esperada a través del número de cuenta
        

    def test_cuentas_pf_mas_10_mil_cup(self):
        self.banco.ingresarCliente(self.cliente)
        self.banco.ingresarComercial(self.comercial)
        self.banco.ingresarCuentaSimple(self.cuenta_simp)
        self.banco.ingresarCuentaFF(self.cuenta_ff)
        self.banco.ingresarCuentaPF(self.cuenta_pf)

        #Comprobando si manda error al no existir cuentas pf con más de 10 mil pesos
        with self.assertRaises(Exception):
            self.banco.cuentasPFmas10MilCUP()

        #Modificando cuenta_pf2 para que tenga más de 10 mil pesos y se pueda ingresar
        self.cuenta_pf2.num_cuenta = "0325469887421243"
        self.cuenta_pf2.saldo = 11000
        self.banco.ingresarCuentaPF(self.cuenta_pf2)
        
        #Cambiando el tipo de moneda de cuenta_pf a EUR para que cumpla la condición de que tenga más de 10000 pesos
        self.cuenta_pf.tipo_moneda = "EUR"

        #Ingresando una nueva cuenta para tener más datos de prueba y cuyo número de cuenta es menor que el anterior para asegurarme de que las cuentas están desordenadas
        cuenta_pf3 = CuentaPF("0325469887421234", "03031976450", "03031976400", 2800.00, "USD", "2021-05-28", "2017-03-25", 5)
        self.banco.ingresarCuentaPF(cuenta_pf3)


        lista_cuentas = self.banco.cuentasPFmas10MilCUP()

        comp_menor = int(lista_cuentas[0].num_cuenta) < int(lista_cuentas[1].num_cuenta) and int(lista_cuentas[0].num_cuenta) < int(lista_cuentas[2].num_cuenta) #Comprobando que el primer número de cuenta de la lista es el menor
        comp_menor2 = int(lista_cuentas[1].num_cuenta) < int(lista_cuentas[2].num_cuenta) #Comprobando que el segundo número de cuenta es menor que el tercero

        #AssertTrue comprueba que el parámetro que se le pasa es verdadero, de cumplirse la condición, entonces están ordenados ascendentemente por el número de cuenta
        self.assertTrue(comp_menor)
        self.assertTrue(comp_menor2)


        