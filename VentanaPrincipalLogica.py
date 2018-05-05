from PyQt5.QtWidgets import QMainWindow, QApplication

from ui.VentanaPrincipal import Ui_MainWindow
from ui.VentanaRespuestaLogica import VentanaRespuestaLogica
import pandas as pd
import sys


class VentanaPrincipalLogica(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        self.ui.btnVerRespuestas.clicked.connect(self.pasar_ventana_respuestas)

        datos = pd.read_csv('compras.csv', header=0)
        print(type(datos))


    def pasar_ventana_respuestas(self):
        self.ventana_respuesta = VentanaRespuestaLogica()
        self.ventana_respuesta.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipalLogica()
    ventana.show()
    sys.exit(app.exec_())
