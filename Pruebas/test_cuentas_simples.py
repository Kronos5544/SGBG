import unittest
from datetime import date
from Modelo.CuentaSimple import CuentaSimple

class TestCuentaSimple(unittest.TestCase):
    def setUp(self):
        self.cuenta = CuentaSimple("0325469887421245", "03031976450", "03031976400", 8000.00, "CUP", "2021-05-28", "2022-03-25")

    def test_property_and_setter(self):
        self.assertEqual(self.cuenta.num_cuenta, "0325469887421245")
        self.cuenta.num_cuenta = "0325478965412547"
        self.assertEqual(self.cuenta.num_cuenta, '0325478965412547')

        self.assertEqual(self.cuenta.cliente, '03031976450')
        self.cuenta.cliente = '03031976400'
        self.assertEqual(self.cuenta.cliente, '03031976400')

        self.assertEqual(self.cuenta.datos_comercial, '03031976400')
        self.cuenta.datos_comercial = '03031976540'
        self.assertEqual(self.cuenta.datos_comercial, '03031976540')

        self.assertEqual(self.cuenta.saldo, 8000.00)
        self.cuenta.saldo = 5840.00
        self.assertEqual(self.cuenta.saldo, 5840.00)

        self.assertEqual(self.cuenta.tipo_moneda, 'CUP')
        self.cuenta.tipo_moneda = 'EUR'
        self.assertEqual(self.cuenta.tipo_moneda, 'EUR')

        self.assertEqual(self.cuenta.fecha_apertura, date(2021,5,28))
        self.cuenta.fecha_apertura = '2022-05-15'
        self.assertEqual(self.cuenta.fecha_apertura, date(2022,5,15))

        self.assertEqual(self.cuenta.fecha_ult_retiro, date(2022,3,25))
        self.cuenta.fecha_ult_retiro = '2022-07-18'
        self.assertEqual(self.cuenta.fecha_ult_retiro, date(2022,7,18))

    def test_calcular_interes(self):
        self.assertEqual(self.cuenta.calcularInteres(), 320)

    def test_depositar_retirar(self):
        self.cuenta + 500.00
        calc_manual = 8000 + round(8000.00 * 0.04, 2) + 500 #Calculando interes y suma manualmente
        self.assertEqual(self.cuenta.saldo, calc_manual)

        self.cuenta - 1140.00 
        calc_manual2 = calc_manual + round(calc_manual * 0.04, 2) - 1140.00 #Calculando interes y resta manualmente
        self.assertEqual(self.cuenta.saldo, calc_manual2)
        self.assertEqual(self.cuenta.fecha_ult_retiro, date.today())

        
