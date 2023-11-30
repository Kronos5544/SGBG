from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

class AcercaDe(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('./Vista/ui/acerca_de.ui', self)