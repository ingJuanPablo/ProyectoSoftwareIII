from PyQt5.QtWidgets import QMainWindow

from ui.VentanaRespuestas import Ui_MainWindow


class VentanaRespuestaLogica(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
