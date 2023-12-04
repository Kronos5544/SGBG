import unittest
from Modelo.Cliente import Cliente

class TestCliente(unittest.TestCase):
    def setUp(self):
        self.cliente = Cliente("Pepe Antonio", "M", "03031976401", "Paquito Gonzales", "Gerente", 5000.00)

    def test_property_and_setter(self):
        self.assertEqual(self.cliente.nombre, "Pepe Antonio")
        self.cliente.nombre = "Mario Gonzales"
        self.assertEqual(self.cliente.nombre, "Mario Gonzales")

        self.assertEqual(self.cliente.sexo, "M")
        self.cliente.sexo = "F"
        self.assertEqual(self.cliente.sexo, "F")

        self.assertEqual(self.cliente.ci, "03031976401")
        self.cliente.ci = "03031976505"
        self.assertEqual(self.cliente.ci, "03031976505")

        self.assertEqual(self.cliente.centro_trabajo, "Paquito Gonzales")
        self.cliente.centro_trabajo = "Villa Azucar" 
        self.assertEqual(self.cliente.centro_trabajo, "Villa Azucar")

        self.assertEqual(self.cliente.ocupacion, "Gerente")
        self.cliente.ocupacion = "Director"
        self.assertEqual(self.cliente.ocupacion, "Director")

        self.assertEqual(self.cliente.salario, 5000.00)
        self.cliente.salario = 2580.00
        self.assertEqual(self.cliente.salario, 2580.00)
        


