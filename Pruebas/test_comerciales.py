import unittest
from Modelo.Comercial import Comercial

class TestComercial(unittest.TestCase):
    def setUp(self):
        self.comercial = Comercial("Juan Almeida", "M", "03031976800", 5)
    
    def test_property_and_setter(self):
        self.assertEqual(self.comercial.nombre, "Juan Almeida")
        self.comercial.nombre = "Juana Almendares"
        self.assertEqual(self.comercial.nombre, "Juana Almendares")

        self.assertEqual(self.comercial.sexo, "M")
        self.comercial.sexo = "F"
        self.assertEqual(self.comercial.sexo, "F")

        self.assertEqual(self.comercial.ci, "03031976800")
        self.comercial.ci = "03031976400"
        self.assertEqual(self.comercial.ci, "03031976400")

        self.assertEqual(self.comercial.anios_ex, 5)
        self.comercial.anios_ex = 1
        self.assertEqual(self.comercial.anios_ex, 1)


  