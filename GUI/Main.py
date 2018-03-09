# from PySide.QtCore import *
# from PySide.QtGui import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import time
import numpy as np
import pyqtgraph as pg

import Exercise0, Exercise1, Exercise2  ,Home, Results1, Serial
import sys
import testblank

Selected_ex = 1


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.resize(681,411)

        Home_Widget = HomeWidget(self)
        self.central_widget.addWidget(Home_Widget)
        Home_Widget.Exercise_button.mousePressEvent = self.Exercise0
        Home_Widget.Result_button.mousePressEvent = self.Results

    def Results(self,val):
        print 'here'
        Results_Widget = ResultsWidget(self)
        self.central_widget.addWidget(Results_Widget)
        self.central_widget.setCurrentWidget(Results_Widget)
        Results_Widget.Home_button.mousePressEvent = self.Home

    def Exercise0(self,val):
        print 'here'
        Exercise0_Widget = Exercise0Widget(self)
        self.central_widget.addWidget(Exercise0_Widget)
        self.central_widget.setCurrentWidget(Exercise0_Widget)

        Exercise0_Widget.Home_button.mousePressEvent = self.Home
        Exercise0_Widget.Go_button_2.mousePressEvent = self.Exercise1
        Exercise0_Widget.Ex_angle.mousePressEvent = self.Exercise1


    def Exercise1(self,val):

        Exercise_Widget = Exercise1Widget(self)
        Ex0 =  Exercise0Widget(self)
        global Selected_ex

        if Selected_ex == 1:
            print 'ex1'
            Exercise_Widget = Exercise1Widget(self)
        elif Selected_ex == 2:
            print 'ex2'
            Exercise_Widget = Exercise2Widget(self) # need to make alternative exercises 2 and 3
        elif Selected_ex == 3:
            print 'ex3'
            Exercise_Widget = Exercise1Widget(self)

        self.central_widget.addWidget(Exercise_Widget)
        self.central_widget.setCurrentWidget(Exercise_Widget)
        Exercise_Widget.Home_button.mousePressEvent = self.Home

    def Home(self,val):
        Home_Widget = HomeWidget(self)
        self.central_widget.addWidget(Home_Widget)
        self.central_widget.setCurrentWidget(Home_Widget)
        Home_Widget.Exercise_button.mouseReleaseEvent = self.Exercise0
        Home_Widget.Result_button.mousePressEvent = self.Results

class HomeWidget(QWidget ,Home.Ui_Form):
    def __init__(self, parent=None):
        super(HomeWidget, self).__init__(parent)
        self.setupUi(self)


class Exercise0Widget(QWidget, Exercise0.Ui_Form):
    def __init__(self, parent=None):
        super(Exercise0Widget, self).__init__(parent)
        self.setupUi(self)
        self.Tab_1.mousePressEvent = self.tab1
        self.Tab_2.mousePressEvent = self.tab2
        self.Tab_3.mousePressEvent = self.tab3

    def tab1(self,val):
        global Selected_ex
        self.retranslateTAB(1)
        Selected_ex = 1
        print Selected_ex
    def tab2(self,val):
        global Selected_ex
        self.retranslateTAB(2)
        Selected_ex = 2
        print Selected_ex
    def tab3(self,val):
        global Selected_ex
        self.retranslateTAB(3)
        Selected_ex = 3
        print Selected_ex


    def retranslateTAB(self, tab_clicked):
        if tab_clicked == 1:
            self.Tab_1.setPixmap(QPixmap("../../../../Work/HCARD/Images/Assets/ResultsLogoAsset 9.png"))
            self.Tab_2.setPixmap(QPixmap("../../../../Work/HCARD/Images/Assets/ResultsLogoAsset 10.png"))
            self.Tab_3.setPixmap(QPixmap("../../../../Work/HCARD/Images/Assets/ResultsLogoAsset 10.png"))
            self.Exercise_box.setPixmap(QPixmap("../../../../Work/HCARD/Images/Assets/SelectedExerciseBox 1.png"))
        elif tab_clicked == 2:
            self.Tab_2.setPixmap(QPixmap("../../../../Work/HCARD/Images/Assets/ResultsLogoAsset 9.png"))
            self.Tab_1.setPixmap(QPixmap("../../../../Work/HCARD/Images/Assets/ResultsLogoAsset 10.png"))
            self.Tab_3.setPixmap(QPixmap("../../../../Work/HCARD/Images/Assets/ResultsLogoAsset 10.png"))
            self.Exercise_box.setPixmap(QPixmap("../../../../Work/HCARD/Images/Assets/SelectedExerciseBox 2.png"))

        elif tab_clicked == 3:
            self.Tab_3.setPixmap(QPixmap("../../../../Work/HCARD/Images/Assets/ResultsLogoAsset 9.png"))
            self.Tab_2.setPixmap(QPixmap("../../../../Work/HCARD/Images/Assets/ResultsLogoAsset 10.png"))
            self.Tab_1.setPixmap(QPixmap("../../../../Work/HCARD/Images/Assets/ResultsLogoAsset 10.png"))
            self.Exercise_box.setPixmap(QPixmap("../../../../Work/HCARD/Images/Assets/SelectedExerciseBox.png"))

class Exercise1Widget(QWidget, Exercise1.Ui_Form):
    def __init__(self, parent=None):
        super(Exercise1Widget, self).__init__(parent)
        self.setupUi(self)
        self.horizontalSlider.valueChanged.connect(self.pot)
        self.flowerval = 1

        self.horizontalSlider_2.valueChanged.connect(self.flower)

        # self.timer = QTimer()
        # self.timer.timeout.connect(self.serial_control)
        # self.timer.start(100)

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

    def retranslateFlower(self, value):
        flowerpath = "../../../../Work/HCARD/Images/FlowerGrowing/AnimationFlowers%04d.png" % (value)
        print flowerpath
        self.Flower.setPixmap(QPixmap(flowerpath))

    def retranslatePot(self, value):
        canpath = "../../../../Work/HCARD/Images/WateringCan/Can%04d.png" % (value)
        print canpath
        self.Can.setPixmap(QPixmap(canpath))

class Exercise2Widget(QWidget, Exercise2.Ui_Form):
    def __init__(self, parent=None):
        super(Exercise2Widget, self).__init__(parent)
        self.setupUi(self)
        self.angle = 0
        self.horizontalSlider.valueChanged.connect(self.leg)

        # print 'ex 2 init'
    #     # self.timer = QTimer()
    #     # self.timer.timeout.connect(self.serial_control)
    #     # self.timer.start(100)
    #
    # def serial_control(self):
    #     self.angle = Serial.Serial_read()
    #     print self.angle
    #     self.retranslateLeg(self.angle)
    #     # if (self.angle > 160) and self.flowerval <100 :
    #     #     self.flowerval +=1
    #     #     self.flower(self.flowerval)

    def leg(self,val):

        self.angle = self.horizontalSlider.value()
        print self.angle
        self.retranslateLeg(self.angle)

    def retranslateLeg(self, value):
        print value
        print 'here'
        legpath = "../../../../Work/HCARD/Images/LegMovement/LegMove%04d.png" % (value)
        print legpath
        self.Leg.setPixmap(QPixmap(legpath))

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
