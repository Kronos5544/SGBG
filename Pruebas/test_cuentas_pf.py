from Modelo.CuentaPF import CuentaPF
from Pruebas.test_cuentas_simples import TestCuentaSimple

class TestCuentaPF(TestCuentaSimple):
    def setUp(self):
        self.cuenta = CuentaPF("0325469887421245", "03031976450", "03031976400", 8000.00, "CUP", "2021-05-28", "2022-03-25", 5)

    def test_property_and_setter(self):
        super().test_property_and_setter()
        self.assertEqual(self.cuenta.plazo, 5)
        self.cuenta.plazo = 2
        self.assertEqual(self.cuenta.plazo, 2)
