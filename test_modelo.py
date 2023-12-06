import unittest
from Pruebas.test_cliente import TestCliente
from Pruebas.test_comerciales import TestComercial
from Pruebas.test_cuentas_simples import TestCuentaSimple
from Pruebas.test_cuentas_pf import TestCuentaPF
from Pruebas.test_cuentas_ff import TestCuentaFF
from Pruebas.test_banco import TestBanco

if __name__ == '__main__':
    print("\nAntes de realizar las pruebas unitarias asegúrese de tener una copia de seguridad de la Base de datos, puesto que estas serán eliminadas durante las pruebas")
    selec = input("\n¿Está seguro de que desea continuar? Escriba 'S' para continuar, o 'N', o cualquier otra letra para cancelar\n")
    if selec.strip().upper() == 'S':
        print("\nRealizando pruebas unitarias: \n")
        unittest.main(verbosity = 2)