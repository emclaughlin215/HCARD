# from PySide.QtCore import *
# from PySide.QtGui import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import time
import numpy as np
import pyqtgraph as pg

import Exercise1 ,Home, Results1, Serial
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

        Home_Widget.Exercise_button.mousePressEvent = self.Exercise
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
        Exercise1_Widget.Home_button.mousePressEvent = self.Home

    def Home(self,val):
        Home_Widget = HomeWidget(self)
        self.central_widget.addWidget(Home_Widget)
        self.central_widget.setCurrentWidget(Home_Widget)
        Home_Widget.Exercise_button.mouseReleaseEvent = self.Exercise
        Home_Widget.Result_button.mousePressEvent = self.Results

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

        self.timer = QTimer()
        self.timer.timeout.connect(self.serial_control)
        self.timer.start(1)

    def serial_control(self):
        self.angle = Serial.Serial_read()
        print self.angle
        self.retranslatePot(self.angle)
        if (self.angle > 160) and self.flowerval <100 :
            self.flowerval +=1
            self.flower(self.flowerval)


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
        pg.setConfigOption('background', 'w')
        super(ResultsWidget, self).__init__(parent)
        self.setupUi(self)

        points = 100
        X = range(0,points)
        Y = np.exp2(X)

       # # X2 = np.add(100, X)
       #  X2 = range(0,100)
       #
       #  Y2 = np.multiply(X2,2)
       #  Y3 = np.multiply(X2,3)
       #  YT = np.concatenate(Y2,Y3)
       #
       #  #Y2 = np.sin(X2)
       #  print YT
       #  #Y2 = np.exp2(X2)
       #  # p1 = self.Plot.addPlot()
       #  for i in range(2):

        # self.Plot.plot(X2, YT[i], pen=(i,2), symbolBrush=(237, 177, 32), symbolPen='w', symbol='star',symbolSize=20, name="symbol='star'")
        self.Plot.plot(X, Y, pen=(237, 177, 32), symbolBrush=(237, 177, 32), symbolPen='w', symbol='star', symbolSize=20, name="symbol='star'")


        # self.Plot.plot(X2, Y2, pen=(255, 255, 255), symbolBrush=(237, 177, 32), symbolPen='w', symbol='star', symbolSize=20,
        #                name="symbol='star'")
        # self.Plot.plot(X, Y, pen=(237, 177, 32), symbolBrush=(237, 177, 32), symbolPen='w', symbol='star', symbolSize=20,
        #                name="symbol='star'")

app = QApplication(sys.argv)
form = MainWindow()
#form.setFocus()
form.show()
app.exec_()
