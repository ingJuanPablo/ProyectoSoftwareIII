from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from pandas import DataFrame
import pandas as pd

from ui.VentanaRespuestas import Ui_MainWindow


class VentanaRespuestaLogica(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        datos = pd.read_csv('compras.csv', header=0)
        self.iniciar_tabla(datos)

        self.ui.btnVolver.clicked.connect(self.action_button_volver)

    def iniciar_tabla(self, datos: DataFrame):
        self.ui.tableRespuestas.setColumnCount(20)
        self.ui.tableRespuestas.setHorizontalHeaderLabels(
            ['Columna1', 'Columna1', 'Columna1', 'Columna4', 'Columna1', 'Columna1', 'Columna1', 'Columna8', 'Columna1',
             'Columna1', 'Columna1', 'Columna12', 'Columna1', 'Columna1', 'Columna1', 'Columna16', 'Columna1',
             'Columna1', 'Columna1', 'Columna20'])
        row = 0
        for fila in datos.iterrows():
            self.ui.tableRespuestas.insertRow(row)
            columna0 = QTableWidgetItem(str(datos.iloc[row][0]))
            columna1 = QTableWidgetItem(str(datos.iloc[row][1]))
            columna2 = QTableWidgetItem(str(datos.iloc[row][2]))
            columna3 = QTableWidgetItem(str(datos.iloc[row][3]))
            columna4 = QTableWidgetItem(str(datos.iloc[row][4]))
            columna5 = QTableWidgetItem(str(datos.iloc[row][5]))
            columna6 = QTableWidgetItem(str(datos.iloc[row][6]))
            columna7 = QTableWidgetItem(str(datos.iloc[row][7]))
            columna8 = QTableWidgetItem(str(datos.iloc[row][8]))
            columna9 = QTableWidgetItem(str(datos.iloc[row][9]))
            columna10 = QTableWidgetItem(str(datos.iloc[row][10]))
            columna11 = QTableWidgetItem(str(datos.iloc[row][11]))
            columna12 = QTableWidgetItem(str(datos.iloc[row][12]))
            columna13 = QTableWidgetItem(str(datos.iloc[row][13]))
            columna14 = QTableWidgetItem(str(datos.iloc[row][14]))
            columna15 = QTableWidgetItem(str(datos.iloc[row][15]))
            columna16 = QTableWidgetItem(str(datos.iloc[row][16]))
            columna17 = QTableWidgetItem(str(datos.iloc[row][17]))
            columna18 = QTableWidgetItem(str(datos.iloc[row][18]))
            columna19 = QTableWidgetItem(str(datos.iloc[row][19]))

            self.ui.tableRespuestas.setItem(row, 0, columna0)
            self.ui.tableRespuestas.setItem(row, 1, columna1)
            self.ui.tableRespuestas.setItem(row, 2, columna2)
            self.ui.tableRespuestas.setItem(row, 3, columna3)
            self.ui.tableRespuestas.setItem(row, 4, columna4)
            self.ui.tableRespuestas.setItem(row, 5, columna5)
            self.ui.tableRespuestas.setItem(row, 6, columna6)
            self.ui.tableRespuestas.setItem(row, 7, columna7)
            self.ui.tableRespuestas.setItem(row, 8, columna8)
            self.ui.tableRespuestas.setItem(row, 9, columna9)
            self.ui.tableRespuestas.setItem(row, 10, columna10)
            self.ui.tableRespuestas.setItem(row, 11, columna11)
            self.ui.tableRespuestas.setItem(row, 12, columna12)
            self.ui.tableRespuestas.setItem(row, 13, columna13)
            self.ui.tableRespuestas.setItem(row, 14, columna14)
            self.ui.tableRespuestas.setItem(row, 15, columna15)
            self.ui.tableRespuestas.setItem(row, 16, columna16)
            self.ui.tableRespuestas.setItem(row, 17, columna17)
            self.ui.tableRespuestas.setItem(row, 18, columna18)
            self.ui.tableRespuestas.setItem(row, 19, columna19)

            row = row + 1

    #
    #Permite volver a la ventana principal
    #
    def action_button_volver(self):
        self.close()


