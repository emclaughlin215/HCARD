# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Exercise0.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(681, 411)
        self.Exercise_header = QtWidgets.QLabel(Form)
        self.Exercise_header.setGeometry(QtCore.QRect(10, 0, 261, 41))
        self.Exercise_header.setMouseTracking(True)
        self.Exercise_header.setText("")
        self.Exercise_header.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Assets/ResultsHeader.png"))
        self.Exercise_header.setObjectName("Exercise_header")
        self.Exercise_box = QtWidgets.QLabel(Form)
        self.Exercise_box.setGeometry(QtCore.QRect(360, 110, 261, 261))
        self.Exercise_box.setMouseTracking(True)
        self.Exercise_box.setText("")
        self.Exercise_box.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Assets/SelectedExerciseBox 1.png"))
        self.Exercise_box.setObjectName("Exercise_box")
        self.Go_button = QtWidgets.QLabel(Form)
        self.Go_button.setGeometry(QtCore.QRect(540, 270, 141, 141))
        self.Go_button.setMouseTracking(True)
        self.Go_button.setText("")
        self.Go_button.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Assets/GoButtonAsset 3.png"))
        self.Go_button.setObjectName("Go_button")
        self.Tab_1 = QtWidgets.QLabel(Form)
        self.Tab_1.setGeometry(QtCore.QRect(360, 80, 86, 31))
        self.Tab_1.setMouseTracking(True)
        self.Tab_1.setText("")
        self.Tab_1.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Assets/ResultsLogoAsset 9.png"))
        self.Tab_1.setObjectName("Tab_1")
        self.Tab_2 = QtWidgets.QLabel(Form)
        self.Tab_2.setGeometry(QtCore.QRect(446, 80, 86, 31))
        self.Tab_2.setMouseTracking(True)
        self.Tab_2.setText("")
        self.Tab_2.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Assets/ResultsLogoAsset 10.png"))
        self.Tab_2.setObjectName("Tab_2")
        self.Tab_3 = QtWidgets.QLabel(Form)
        self.Tab_3.setGeometry(QtCore.QRect(532, 80, 91, 31))
        self.Tab_3.setMouseTracking(True)
        self.Tab_3.setText("")
        self.Tab_3.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Assets/ResultsLogoAsset 10.png"))
        self.Tab_3.setObjectName("Tab_3")
        self.Home_button = QtWidgets.QLabel(Form)
        self.Home_button.setGeometry(QtCore.QRect(20, 360, 86, 31))
        self.Home_button.setMouseTracking(True)
        self.Home_button.setText("")
        self.Home_button.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Assets/HomearrowleftAsset 3.png"))
        self.Home_button.setObjectName("Home_button")
        self.Star_1 = QtWidgets.QLabel(Form)
        self.Star_1.setGeometry(QtCore.QRect(140, 160, 31, 41))
        self.Star_1.setText("")
        self.Star_1.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Assets/StarAsset 5.png"))
        self.Star_1.setObjectName("Star_1")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(10, 100, 271, 21))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.Star_3 = QtWidgets.QLabel(Form)
        self.Star_3.setGeometry(QtCore.QRect(200, 160, 31, 41))
        self.Star_3.setText("")
        self.Star_3.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Assets/Star_unselectedAsset 6.png"))
        self.Star_3.setObjectName("Star_3")
        self.LastScore_header = QtWidgets.QLabel(Form)
        self.LastScore_header.setGeometry(QtCore.QRect(10, 140, 131, 16))
        font = QtGui.QFont()
        font.setFamily("MS Office Symbol Semilight")
        font.setPointSize(16)
        self.LastScore_header.setFont(font)
        self.LastScore_header.setTextFormat(QtCore.Qt.AutoText)
        self.LastScore_header.setObjectName("LastScore_header")
        self.Advice_header = QtWidgets.QLabel(Form)
        self.Advice_header.setGeometry(QtCore.QRect(10, 210, 101, 16))
        font = QtGui.QFont()
        font.setFamily("MS Office Symbol Semilight")
        font.setPointSize(16)
        self.Advice_header.setFont(font)
        self.Advice_header.setTextFormat(QtCore.Qt.AutoText)
        self.Advice_header.setObjectName("Advice_header")
        self.Star_2 = QtWidgets.QLabel(Form)
        self.Star_2.setGeometry(QtCore.QRect(170, 160, 31, 41))
        self.Star_2.setText("")
        self.Star_2.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Assets/StarAsset 5.png"))
        self.Star_2.setObjectName("Star_2")
        self.Progreamme_progression_header = QtWidgets.QLabel(Form)
        self.Progreamme_progression_header.setGeometry(QtCore.QRect(10, 70, 251, 16))
        font = QtGui.QFont()
        font.setFamily("MS Office Symbol Semilight")
        font.setPointSize(16)
        self.Progreamme_progression_header.setFont(font)
        self.Progreamme_progression_header.setTextFormat(QtCore.Qt.AutoText)
        self.Progreamme_progression_header.setObjectName("Progreamme_progression_header")
        self.Last_angle = QtWidgets.QLabel(Form)
        self.Last_angle.setGeometry(QtCore.QRect(10, 170, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad CAD")
        font.setPointSize(12)
        self.Last_angle.setFont(font)
        self.Last_angle.setObjectName("Last_angle")
        self.Last_advice = QtWidgets.QLabel(Form)
        self.Last_advice.setGeometry(QtCore.QRect(10, 240, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad CAD")
        font.setPointSize(12)
        self.Last_advice.setFont(font)
        self.Last_advice.setObjectName("Last_advice")
        self.Ex_angle = QtWidgets.QLabel(Form)
        self.Ex_angle.setGeometry(QtCore.QRect(550, 320, 111, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(38, 108, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 108, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.Ex_angle.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Ex_angle.setFont(font)
        self.Ex_angle.setObjectName("Ex_angle")
        self.Go_button_2 = QtWidgets.QLabel(Form)
        self.Go_button_2.setGeometry(QtCore.QRect(540, 270, 141, 141))
        self.Go_button_2.setMouseTracking(True)
        self.Go_button_2.setText("")
        self.Go_button_2.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Assets/ExercisebuttonaltAsset 12.png"))
        self.Go_button_2.setObjectName("Go_button_2")
        self.Exercise_header.raise_()
        self.Exercise_box.raise_()
        self.Go_button.raise_()
        self.Tab_1.raise_()
        self.Tab_2.raise_()
        self.Tab_3.raise_()
        self.Home_button.raise_()
        self.Star_1.raise_()
        self.progressBar.raise_()
        self.Star_3.raise_()
        self.LastScore_header.raise_()
        self.Advice_header.raise_()
        self.Star_2.raise_()
        self.Progreamme_progression_header.raise_()
        self.Last_angle.raise_()
        self.Last_advice.raise_()
        self.Go_button_2.raise_()
        self.Ex_angle.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.LastScore_header.setText(_translate("Form", "Last Score:"))
        self.Advice_header.setText(_translate("Form", "Advice:"))
        self.Progreamme_progression_header.setText(_translate("Form", "Programme Progression:"))
        self.Last_angle.setText(_translate("Form", "0 degrees"))
        self.Last_advice.setText(_translate("Form", "Some Text"))
        self.Ex_angle.setText(_translate("Form", "135°"))

