# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Results1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(681, 411)
        Form.setMouseTracking(True)
        self.Home_button = QtWidgets.QLabel(Form)
        self.Home_button.setGeometry(QtCore.QRect(570, 380, 91, 21))
        self.Home_button.setMouseTracking(True)
        self.Home_button.setText("")
        self.Home_button.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Assets/homearrowAsset 1.png"))
        self.Home_button.setObjectName("Home_button")
        self.Header = QtWidgets.QLabel(Form)
        self.Header.setGeometry(QtCore.QRect(10, 10, 171, 41))
        self.Header.setMouseTracking(True)
        self.Header.setText("")
        self.Header.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Assets/ResultsheaderAsset 2.png"))
        self.Header.setObjectName("Header")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

