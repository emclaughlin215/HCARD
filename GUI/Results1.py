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
        self.Header = QtWidgets.QLabel(Form)
        self.Header.setGeometry(QtCore.QRect(10, 10, 171, 41))
        self.Header.setMouseTracking(True)
        self.Header.setText("")
        self.Header.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Assets/ResultsheaderAsset 2.png"))
        self.Header.setObjectName("Header")
        self.Home_button = QtWidgets.QLabel(Form)
        self.Home_button.setGeometry(QtCore.QRect(20, 360, 91, 41))
        self.Home_button.setMouseTracking(True)
        self.Home_button.setText("")
        self.Home_button.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Assets/HomearrowleftAsset 3.png"))
        self.Home_button.setObjectName("Home_button")
        self.Plot = PlotWidget(Form)
        self.Plot.setGeometry(QtCore.QRect(20, 70, 481, 271))
        self.Plot.setObjectName("Plot")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

from pyqtgraph import PlotWidget
