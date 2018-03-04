# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Exercise1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(681, 411)
        self.Flower = QtWidgets.QLabel(Form)
        self.Flower.setGeometry(QtCore.QRect(0, 0, 681, 411))
        self.Flower.setText("")
        self.Flower.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/FlowerGrowing/AnimationFlowers0001.png"))
        self.Flower.setObjectName("Flower")
        self.Can = QtWidgets.QLabel(Form)
        self.Can.setGeometry(QtCore.QRect(0, 0, 681, 411))
        self.Can.setText("")
        self.Can.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/WateringCan/Can0001.png"))
        self.Can.setObjectName("Can")

        self.Flower.raise_()
        self.Can.raise_()

        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(430, 90, 160, 19))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider_2 = QtWidgets.QSlider(Form)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(430, 120, 160, 19))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider.setValue(1)
        self.horizontalSlider_2.setValue(1)
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(90)
        self.horizontalSlider_2.setMinimum(1)
        self.horizontalSlider_2.setMaximum(100)

        self.Home_button = QtWidgets.QLabel(Form)
        self.Home_button.setGeometry(QtCore.QRect(20, 360, 91, 41))
        self.Home_button.setMouseTracking(True)
        self.Home_button.setText("")
        self.Home_button.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Assets/HomearrowleftAsset 3.png"))
        self.Home_button.setObjectName("Home_button")


        self.horizontalSlider.raise_()
        self.horizontalSlider_2.raise_()
        self.Home_button.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    def retranslateFlower(self, value):
        flowerpath = "../../../../Work/HCARD/Images/FlowerGrowing/AnimationFlowers%04d.png" %(value)
        print flowerpath
        self.Flower.setPixmap(QtGui.QPixmap(flowerpath))

    def retranslatePot(self, value):
        canpath = "../../../../Work/HCARD/Images/WateringCan/Can%04d.png" %(value)
        print canpath
        self.Can.setPixmap(QtGui.QPixmap(canpath))