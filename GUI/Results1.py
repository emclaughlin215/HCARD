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
        self.Plot.setMouseTracking(True)
        self.Plot.setObjectName("Plot")
        self.achievedheader = QtWidgets.QLabel(Form)
        self.achievedheader.setGeometry(QtCore.QRect(520, 70, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.achievedheader.setFont(font)
        self.achievedheader.setObjectName("achievedheader")
        self.youare = QtWidgets.QLabel(Form)
        self.youare.setGeometry(QtCore.QRect(520, 150, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.youare.setFont(font)
        self.youare.setObjectName("youare")
        self.legend = QtWidgets.QLabel(Form)
        self.legend.setGeometry(QtCore.QRect(260, 350, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.legend.setFont(font)
        self.legend.setText("")
        self.legend.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Assets/LegendAsset 4.png"))
        self.legend.setObjectName("legend")
        self.Current_angle = QtWidgets.QLabel(Form)
        self.Current_angle.setGeometry(QtCore.QRect(560, 120, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Current_angle.setFont(font)
        self.Current_angle.setObjectName("Current_angle")
        self.deg1 = QtWidgets.QLabel(Form)
        self.deg1.setGeometry(QtCore.QRect(600, 110, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.deg1.setFont(font)
        self.deg1.setObjectName("deg1")
        self.social = QtWidgets.QLabel(Form)
        self.social.setGeometry(QtCore.QRect(520, 350, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.social.setFont(font)
        self.social.setText("")
        self.social.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Assets/SocialAsset 1.png"))
        self.social.setObjectName("social")
        self.Current_progression = QtWidgets.QLabel(Form)
        self.Current_progression.setGeometry(QtCore.QRect(560, 200, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Current_progression.setFont(font)
        self.Current_progression.setObjectName("Current_progression")
        self.deg1_2 = QtWidgets.QLabel(Form)
        self.deg1_2.setGeometry(QtCore.QRect(600, 190, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.deg1_2.setFont(font)
        self.deg1_2.setObjectName("deg1_2")
        self.Schedule_state_2 = QtWidgets.QLabel(Form)
        self.Schedule_state_2.setGeometry(QtCore.QRect(540, 250, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Schedule_state_2.setFont(font)
        self.Schedule_state_2.setObjectName("Schedule_state_2")
        self.Schedule_state_3 = QtWidgets.QLabel(Form)
        self.Schedule_state_3.setGeometry(QtCore.QRect(520, 270, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Schedule_state_3.setFont(font)
        self.Schedule_state_3.setObjectName("Schedule_state_3")
        self.Axis_X = QtWidgets.QLabel(Form)
        self.Axis_X.setGeometry(QtCore.QRect(240, 330, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Axis_X.setFont(font)
        self.Axis_X.setText("")
        self.Axis_X.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Assets/AxislabelsAsset 4.png"))
        self.Axis_X.setObjectName("Axis_X")
        self.Axis_Y = QtWidgets.QLabel(Form)
        self.Axis_Y.setGeometry(QtCore.QRect(10, 120, 21, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Axis_Y.setFont(font)
        self.Axis_Y.setText("")
        self.Axis_Y.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Assets/AxislabelsAsset 5.png"))
        self.Axis_Y.setObjectName("Axis_Y")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.achievedheader.setText(_translate("Form", "Achieved:"))
        self.youare.setText(_translate("Form", "You are:"))
        self.Current_angle.setText(_translate("Form", "90"))
        self.deg1.setText(_translate("Form", "°"))
        self.Current_progression.setText(_translate("Form", "90"))
        self.deg1_2.setText(_translate("Form", "%"))
        self.Schedule_state_2.setText(_translate("Form", "Through your "))
        self.Schedule_state_3.setText(_translate("Form", "exercise programme"))

from pyqtgraph import PlotWidget
