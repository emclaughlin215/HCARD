# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Home.ui'
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
        self.Exercise_button = QtWidgets.QLabel(Form)
        self.Exercise_button.setGeometry(QtCore.QRect(150, 130, 181, 141))
        self.Exercise_button.setMouseTracking(True)
        self.Exercise_button.setText("")
        self.Exercise_button.setPixmap(QtGui.QPixmap("Graphics/Assets/ExerciseLogoAsset 2.png"))
        self.Exercise_button.setOpenExternalLinks(False)
        self.Exercise_button.setObjectName("Exercise_button")
        self.Result_button = QtWidgets.QLabel(Form)
        self.Result_button.setGeometry(QtCore.QRect(330, 130, 181, 141))
        self.Result_button.setMouseTracking(True)
        self.Result_button.setText("")
        self.Result_button.setPixmap(QtGui.QPixmap("Graphics/Assets/ResultsLogoAsset 4.png"))
        self.Result_button.setObjectName("Result_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

