from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

import TestButton
import sys
class RunButton(QWidget, TestButton.Ui_Form):
    def __init__(self, parent=None):
        super(RunButton, self).__init__(parent)
        self.setupUi(self)
        self.Button1.mousePressEvent = self.retranslateText




app = QApplication(sys.argv)
form = RunButton()
#form.setFocus()
form.show()
app.exec_()


