# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Exercise1.2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(681, 411)
        self.Leg = QtWidgets.QLabel(Form)
        self.Leg.setGeometry(QtCore.QRect(0, 0, 681, 411))
        self.Leg.setText("")
        self.Leg.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/LegMovement/LegMove0001.png"))
        self.Leg.setObjectName("Leg")
        self.Home_button = QtWidgets.QLabel(Form)
        self.Home_button.setGeometry(QtCore.QRect(20, 370, 86, 31))
        self.Home_button.setMouseTracking(True)
        self.Home_button.setText("")
        self.Home_button.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Assets/HomearrowleftAsset 3.png"))
        self.Home_button.setObjectName("Home_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

