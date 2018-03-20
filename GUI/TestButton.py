# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestButton.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(681, 411)
        self.Button1 = QtWidgets.QLabel(Form)
        self.Button1.setGeometry(QtCore.QRect(240, 150, 131, 131))
        self.Button1.setMouseTracking(True)
        self.Button1.setText("")
        self.Button1.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Assets/GoButtonAsset 3.png"))
        self.Button1.setObjectName("Button1")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 90, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Myriad CAD")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    def retranslateText(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Form", "Mar es un puta madre"))


