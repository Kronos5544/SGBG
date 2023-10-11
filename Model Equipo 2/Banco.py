from Comercial import Comercial
from Cliente import Cliente
from CuentaSimple import CuentaSimple
from CuentaPF import CuentaPL
from CuentaFF import CuentaFF

class Banco():
    def __init__(self):
        self.listaCuentaSimple = []
        self.listaCuentaFF = []
        self.listaCuentaPF = []
        self.listaCliente = []
        self.listaComercial = []

    def ingresarCliente(self, nombre, sexo, ci, centro_trabajo, ocupacion, salario):
        cliente = Cliente(nombre, sexo, ci, centro_trabajo, ocupacion, salario)
        self.listaCliente.append(cliente)
