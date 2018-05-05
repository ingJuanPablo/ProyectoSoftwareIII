# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaRespuestas.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableRespuestas = QtWidgets.QTableWidget(self.centralwidget)
        self.tableRespuestas.setGeometry(QtCore.QRect(20, 80, 761, 481))
        self.tableRespuestas.setObjectName("tableRespuestas")
        self.tableRespuestas.setColumnCount(0)
        self.tableRespuestas.setRowCount(0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(6, 20, 791, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.menuAbrirArchivo = QtWidgets.QAction(MainWindow)
        self.menuAbrirArchivo.setObjectName("menuAbrirArchivo")
        self.menuArchivo.addAction(self.menuAbrirArchivo)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Respuestas"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuAbrirArchivo.setText(_translate("MainWindow", "Abrir archivo"))

