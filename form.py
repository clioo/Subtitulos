# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
class Ui_MainWindow(QtWidgets):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.initUI()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(565, 342)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cmd_fileExplorer = QtWidgets.QPushButton(self.centralwidget)
        self.cmd_fileExplorer.setGeometry(QtCore.QRect(400, 20, 75, 23))
        self.cmd_fileExplorer.setObjectName("cmd_fileExplorer")
        self.txt_DragAndDrop = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_DragAndDrop.setGeometry(QtCore.QRect(40, 50, 471, 231))
        self.txt_DragAndDrop.setObjectName("txt_DragAndDrop")
        self.txt_ruta = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_ruta.setGeometry(QtCore.QRect(100, 20, 291, 21))
        self.txt_ruta.setObjectName("txt_ruta")
        self.cmd_Descargar = QtWidgets.QPushButton(self.centralwidget)
        self.cmd_Descargar.setGeometry(QtCore.QRect(410, 280, 101, 41))
        self.cmd_Descargar.setObjectName("cmd_Descargar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Subtitulos"))
        self.cmd_fileExplorer.setText(_translate("MainWindow", "..."))
        self.cmd_Descargar.setText(_translate("MainWindow", "Descargar"))

app = QApplication(sys.argv)
window = Ui_MainWindow()
window.show()
sys.exit(app.exec_())
