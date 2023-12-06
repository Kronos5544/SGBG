from Modelo.CuentaPF import CuentaPF
from Pruebas.test_cuentas_simples import TestCuentaSimple

class TestCuentaPF(TestCuentaSimple):
    def setUp(self):
        self.cuenta = CuentaPF("0325469887421245", "03031976450", "03031976400", 8000.00, "CUP", "2021-05-28", "2022-03-25", 1)

    def test_property_and_setter(self):
        super().test_property_and_setter()
        self.assertEqual(self.cuenta.plazo, 1)
        self.cuenta.plazo = 2
        self.assertEqual(self.cuenta.plazo, 2)
    
    def test_calcular_interes(self):
        self.assertEqual(self.cuenta.calcularInteres(), 640)

    def test_depositar_retirar(self):

        self.cuenta + 700.00
        self.assertEqual(self.cuenta.saldo, 8700)

        #Comprobando que si no se cumple el plazo no se suma el interes
        self.cuenta.plazo = 5
        self.cuenta - 400 
        self.assertEqual(self.cuenta.saldo, 8300)

        #Comprobando que se suma el interes si se cumple el plazo
        self.cuenta.fecha_ult_retiro = "2022-03-25"
        self.cuenta.plazo = 1
        self.cuenta - 800.00
        calc_manual = 8300 + (8300 * 0.08) - 800
        self.assertEqual(self.cuenta.saldo, calc_manual)

        
