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
        MainWindow.resize(800, 591)
        MainWindow.setStyleSheet("#btnVolver:hover{\n"
"background-color: rgb(65, 195, 0);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 791, 551))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.tableRespuestas = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableRespuestas.setObjectName("tableRespuestas")
        self.tableRespuestas.setColumnCount(0)
        self.tableRespuestas.setRowCount(0)
        self.gridLayout.addWidget(self.tableRespuestas, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btnVolver = QtWidgets.QPushButton(self.gridLayoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Angel/Pictures/icons8-retroceder-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnVolver.setIcon(icon)
        self.btnVolver.setIconSize(QtCore.QSize(32, 32))
        self.btnVolver.setObjectName("btnVolver")
        self.horizontalLayout_2.addWidget(self.btnVolver)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
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
        self.btnVolver.setText(_translate("MainWindow", "VOLVER"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuAbrirArchivo.setText(_translate("MainWindow", "Abrir archivo"))

