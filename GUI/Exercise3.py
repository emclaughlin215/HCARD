# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Exercise3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(681, 411)
        self.Last_angle = QtWidgets.QLabel(Form)
        self.Last_angle.setGeometry(QtCore.QRect(310, 160, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad CAD")
        font.setPointSize(12)
        self.Last_angle.setFont(font)
        self.Last_angle.setObjectName("Last_angle")
        self.Star_1 = QtWidgets.QLabel(Form)
        self.Star_1.setGeometry(QtCore.QRect(320, 50, 71, 71))
        self.Star_1.setText("")
        self.Star_1.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Assets/Star_largeAsset 2.png"))
        self.Star_1.setObjectName("Star_1")
        self.Progreamme_progression_header = QtWidgets.QLabel(Form)
        self.Progreamme_progression_header.setGeometry(QtCore.QRect(20, 60, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Office Symbol Semilight")
        font.setPointSize(16)
        self.Progreamme_progression_header.setFont(font)
        self.Progreamme_progression_header.setTextFormat(QtCore.Qt.AutoText)
        self.Progreamme_progression_header.setObjectName("Progreamme_progression_header")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(20, 100, 271, 21))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.Progreamme_progression_header_2 = QtWidgets.QLabel(Form)
        self.Progreamme_progression_header_2.setGeometry(QtCore.QRect(310, 180, 381, 51))
        font = QtGui.QFont()
        font.setFamily("MS Office Symbol Semilight")
        font.setPointSize(20)
        self.Progreamme_progression_header_2.setFont(font)
        self.Progreamme_progression_header_2.setTextFormat(QtCore.Qt.AutoText)
        self.Progreamme_progression_header_2.setObjectName("Progreamme_progression_header_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Small_image_1 = QtWidgets.QLabel(Form)
        self.Small_image_1.setGeometry(QtCore.QRect(40, 190, 91, 131))
        self.Small_image_1.setText("")
        self.Small_image_1.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Targetsmall/Targetsmall0001.png"))
        self.Small_image_1.setOpenExternalLinks(False)
        self.Small_image_1.setObjectName("Small_image_1")
        self.Star_2 = QtWidgets.QLabel(Form)
        self.Star_2.setGeometry(QtCore.QRect(450, 50, 71, 71))
        self.Star_2.setText("")
        self.Star_2.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Assets/Star_largeAsset 2.png"))
        self.Star_2.setObjectName("Star_2")
        self.Star_3 = QtWidgets.QLabel(Form)
        self.Star_3.setGeometry(QtCore.QRect(580, 50, 71, 71))
        self.Star_3.setText("")
        self.Star_3.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Assets/Star_largeAsset 2.png"))
        self.Star_3.setObjectName("Star_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(1000, 1000, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.Small_image_2 = QtWidgets.QLabel(Form)
        self.Small_image_2.setGeometry(QtCore.QRect(80, 190, 91, 131))
        self.Small_image_2.setText("")
        self.Small_image_2.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Targetsmall/Targetsmall0001.png"))
        self.Small_image_2.setOpenExternalLinks(False)
        self.Small_image_2.setObjectName("Small_image_2")
        self.Small_image_3 = QtWidgets.QLabel(Form)
        self.Small_image_3.setGeometry(QtCore.QRect(120, 190, 91, 131))
        self.Small_image_3.setText("")
        self.Small_image_3.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Targetsmall/Targetsmall0001.png"))
        self.Small_image_3.setOpenExternalLinks(False)
        self.Small_image_3.setObjectName("Small_image_3")
        self.Small_image_4 = QtWidgets.QLabel(Form)
        self.Small_image_4.setGeometry(QtCore.QRect(160, 190, 91, 131))
        self.Small_image_4.setText("")
        self.Small_image_4.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Targetsmall/Targetsmall0001.png"))
        self.Small_image_4.setOpenExternalLinks(False)
        self.Small_image_4.setObjectName("Small_image_4")
        self.Small_image_5 = QtWidgets.QLabel(Form)
        self.Small_image_5.setGeometry(QtCore.QRect(200, 190, 91, 131))
        self.Small_image_5.setText("")
        self.Small_image_5.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Targetsmall/Targetsmall0001.png"))
        self.Small_image_5.setOpenExternalLinks(False)
        self.Small_image_5.setObjectName("Small_image_5")
        self.Small_image_6 = QtWidgets.QLabel(Form)
        self.Small_image_6.setGeometry(QtCore.QRect(80, 270, 91, 131))
        self.Small_image_6.setText("")
        self.Small_image_6.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Targetsmall/Targetsmall0001.png"))
        self.Small_image_6.setOpenExternalLinks(False)
        self.Small_image_6.setObjectName("Small_image_6")
        self.Small_image_7 = QtWidgets.QLabel(Form)
        self.Small_image_7.setGeometry(QtCore.QRect(120, 270, 91, 131))
        self.Small_image_7.setText("")
        self.Small_image_7.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Targetsmall/Targetsmall0001.png"))
        self.Small_image_7.setOpenExternalLinks(False)
        self.Small_image_7.setObjectName("Small_image_7")
        self.Small_image_8 = QtWidgets.QLabel(Form)
        self.Small_image_8.setGeometry(QtCore.QRect(40, 270, 91, 131))
        self.Small_image_8.setText("")
        self.Small_image_8.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Targetsmall/Targetsmall0001.png"))
        self.Small_image_8.setOpenExternalLinks(False)
        self.Small_image_8.setObjectName("Small_image_8")
        self.Small_image_9 = QtWidgets.QLabel(Form)
        self.Small_image_9.setGeometry(QtCore.QRect(160, 270, 91, 131))
        self.Small_image_9.setText("")
        self.Small_image_9.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Targetsmall/Targetsmall0001.png"))
        self.Small_image_9.setOpenExternalLinks(False)
        self.Small_image_9.setObjectName("Small_image_9")
        self.Small_image_10 = QtWidgets.QLabel(Form)
        self.Small_image_10.setGeometry(QtCore.QRect(200, 270, 91, 131))
        self.Small_image_10.setText("")
        self.Small_image_10.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Targetsmall/Targetsmall0001.png"))
        self.Small_image_10.setOpenExternalLinks(False)
        self.Small_image_10.setObjectName("Small_image_10")
        self.comment = QtWidgets.QLineEdit(Form)
        self.comment.setGeometry(QtCore.QRect(310, 250, 351, 31))
        self.comment.setText("")
        self.comment.setObjectName("comment")
        self.saveButton = QtWidgets.QLabel(Form)
        self.saveButton.setGeometry(QtCore.QRect(540, 320, 111, 71))
        self.saveButton.setText("")
        self.saveButton.setPixmap(QtGui.QPixmap("../../../../Work/HCARD/Images/Assets/SaveAsset 3.png"))
        self.saveButton.setObjectName("saveButton")
        self.Advice_progression_header_3 = QtWidgets.QLabel(Form)
        self.Advice_progression_header_3.setGeometry(QtCore.QRect(20, 130, 251, 41))
        font = QtGui.QFont()
        font.setFamily("MS Office Symbol Semilight")
        font.setPointSize(16)
        self.Advice_progression_header_3.setFont(font)
        self.Advice_progression_header_3.setTextFormat(QtCore.Qt.AutoText)
        self.Advice_progression_header_3.setObjectName("Advice_progression_header_3")
        self.advice_label = QtWidgets.QLabel(Form)
        self.advice_label.setGeometry(QtCore.QRect(20, 170, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad CAD")
        font.setPointSize(12)
        self.advice_label.setFont(font)
        self.advice_label.setObjectName("advice_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Last_angle.setText(_translate("Form", "0 degrees"))
        self.Progreamme_progression_header.setText(_translate("Form", "Programme Progression:"))
        self.Progreamme_progression_header_2.setText(_translate("Form", "How did you find the exercise?"))
        self.label_2.setText(_translate("Form", "Well Done!"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.comment.setPlaceholderText(_translate("Form", "Please write a short comment on the previous exercise here..."))
        self.Advice_progression_header_3.setText(_translate("Form", "Advice:"))
        self.advice_label.setText(_translate("Form", "Try holding for a bit longer!"))

