# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.btnGo = QtWidgets.QPushButton(self.centralWidget)
        self.btnGo.setGeometry(QtCore.QRect(540, 350, 51, 32))
        self.btnGo.setObjectName("btnGo")
        self.btnShort = QtWidgets.QPushButton(self.centralWidget)
        self.btnShort.setGeometry(QtCore.QRect(540, 410, 101, 32))
        self.btnShort.setObjectName("btnShort")
        self.btnPassFail = QtWidgets.QPushButton(self.centralWidget)
        self.btnPassFail.setGeometry(QtCore.QRect(530, 470, 113, 32))
        self.btnPassFail.setObjectName("btnPassFail")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnGo.setText(_translate("MainWindow", "Start"))
        self.btnShort.setText(_translate("MainWindow", "Short Check"))
        self.btnPassFail.setText(_translate("MainWindow", "Pass/Fail"))

