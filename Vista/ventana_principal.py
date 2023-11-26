from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QCloseEvent, QResizeEvent
from PyQt5 import uic

class MainWindow(QMainWindow):
    def __init__(self, presentador):
        self.__presentador = presentador
        QMainWindow.__init__(self)
        uic.loadUi('Vista/ui/ventana_principal.ui', self)

        self.actionSalir.triggered.connect(self.close)
        self.actionAcerca_de.triggered.connect(self.__presentador.acerca_de)

    def resizeEvent(self, a0: QResizeEvent):
        logo = QPixmap('./Vista/media/logo.png')
        logo = logo.scaled(self.size(), Qt.IgnoreAspectRatio)  # KeepAspectRatio, KeepAspectRatioByExpanding
        pal = self.palette()
        pal.setBrush(QPalette.Background, QBrush(logo))
        self.setPalette(pal)


    def closeEvent(self, a0: QCloseEvent):
        QMainWindow.closeEvent(self, a0)
