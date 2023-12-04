from Modelo.CuentaFF import CuentaFF
from Pruebas.test_cuentas_simples import TestCuentaSimple

class TestCuentaFF(TestCuentaSimple):
    def setUp(self):
        self.cuenta = CuentaFF("0325469887421245", "03031976450", "03031976400", 8000.00, "CUP", "2021-05-28", "2022-03-25", 200.00)

    def test_property_and_setter(self):
        super().test_property_and_setter()
        self.assertEqual(self.cuenta.cuota_mensual, 200.00)
        self.cuenta.cuota_mensual = 700.00
        self.assertEqual(self.cuenta.cuota_mensual, 700.00)

    def test_calcular_interes(self):
        self.assertEqual(self.cuenta.calcularInteres(), 480)