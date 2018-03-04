# from PySide.QtCore import *
# from PySide.QtGui import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import time

import Exercise1 , Home, Results1
import sys
import testblank

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.resize(681,411)


        Home_Widget = HomeWidget(self)
        self.central_widget.addWidget(Home_Widget)

        Home_Widget.Exercise_button.mouseReleaseEvent = self.Exercise
        Home_Widget.Result_button.mousePressEvent = self.Results

    def Results(self,val):
        print 'here'
        Results_Widget = ResultsWidget(self)
        self.central_widget.addWidget(Results_Widget)
        self.central_widget.setCurrentWidget(Results_Widget)
        Results_Widget.Home_button.mousePressEvent = self.Home

    def Exercise(self,val):
        print 'here'
        Exercise1_Widget = Exercise1Widget(self)
        self.central_widget.addWidget(Exercise1_Widget)
        self.central_widget.setCurrentWidget(Exercise1_Widget)

    def Home(self,val):
        Home_Widget = HomeWidget(self)
        self.central_widget.addWidget(Home_Widget)
        self.central_widget.setCurrentWidget(Home_Widget)
        Home_Widget.Exercise_button.mouseReleaseEvent = self.Results
        Home_Widget.Result_button.mousePressEvent = self.Exercise



class HomeWidget(QWidget ,Home.Ui_Form):
    def __init__(self, parent=None):
        super(HomeWidget, self).__init__(parent)
        self.setupUi(self)

class Exercise1Widget(QWidget, Exercise1.Ui_Form):
    def __init__(self, parent=None):
        super(Exercise1Widget, self).__init__(parent)
        self.setupUi(self)
        self.horizontalSlider.valueChanged.connect(self.pot)
        self.flowerval = 1

        self.horizontalSlider_2.valueChanged.connect(self.flower)

    def pot(self, value):
        print (value)
        self.retranslatePot(value)
        if (self.horizontalSlider.value() > 70) and self.flowerval <100 :
            self.flowerval +=1
            self.flower(self.flowerval)


    def flower(self,value):
        print (value)
        self.retranslateFlower(value)

class ResultsWidget(QWidget , Results1.Ui_Form):
    def __init__(self, parent=None):
        super(ResultsWidget, self).__init__(parent)
        self.setupUi(self)



app = QApplication(sys.argv)
form = MainWindow()
#form.setFocus()
form.show()
app.exec_()
