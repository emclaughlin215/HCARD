# from PySide.QtCore import *
# from PySide.QtGui import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import time
import numpy as np
import pyqtgraph as pg
import datetime

import Exercise0, Exercise1, Exercise2  ,Home, Results1, Serial, Data_target, Data
import sys
import testblank

Selected_ex = 1
Selected_ex_angle = 0


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
        self.exercise_list = Data.loadObjects('Data_backend.txt')
        self.loaddata()

    def loaddata(self):
        ## still need to set progression %
        self.ex1 = self.exercise_list[-1]
        target_angle = self.ex1.Target_A
        target_angle_str =  str(target_angle + " degrees")
        self.Last_angle.setText(target_angle_str)
        self.Last_advice.setText(str(self.ex1.Advice))
        self.score = int(self.ex1.Score)
        self.star_list = [self.Star_1,self.Star_2, self.Star_3]
        for i in range(0,int(self.score)):
            self.star_list[i].setPixmap(QPixmap("../../../../Work/HCARD/Images/Assets/StarAsset 5.png"))
        if self.score == 3:
            self.exercise_angle = int(target_angle)+5
        else:
            self.exercise_angle = int(target_angle)

        global selected_ex_angle
        selected_ex_angle = self.exercise_angle
        self.Ex_angle.setText(str(self.exercise_angle))

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
        global selected_ex_angle
        self.targetAngle = selected_ex_angle
        self.midmove = False
        self.movecount = 0
        self.smallflowerlist = [self.Flower_small_1,self.Flower_small_2,self.Flower_small_3,self.Flower_small_4,self.Flower_small_5,self.Flower_small_6,self.Flower_small_7,self.Flower_small_8,self.Flower_small_9,self.Flower_small_10]

        self.horizontalSlider_2.valueChanged.connect(self.flower)
    #
    #     self.timer = QTimer()
    #     self.timer.timeout.connect(self.serial_control)
    #     self.timer.start(100)
    #
    # def serial_control(self):
    #     self.angle = Serial.Serial_read()
    #     # print self.angle
    #     self.retranslatePot(self.angle) # replace with self.pot(self.angle)
    #     if (self.targetAngle+5>self.angle>self.targetAngle-5) and self.flowerval <100:
    #         self.flowerval +=1
    #         self.flower(self.flowerval)

    def pot(self, value):
        # print (value)
        self.retranslatePot(value)
        if (value > self.targetAngle-5) and (value< self.targetAngle+5) and self.flowerval <100 and self.movecount <10:
            self.flowerval +=1
            self.flower(self.flowerval)

    def flower(self,value):
        # print (value)
        self.retranslateFlower(value)

    def retranslateFlower(self, value):
        flowerpath = "../../../../Work/HCARD/Images/FlowerGrowing/AnimationFlowers%04d.png" % (value)
        # print flowerpath
        self.Flower.setPixmap(QPixmap(flowerpath))

    def retranslatePot(self, value):
        print self.movecount
        print self.midmove
        # print value
        if value > 2:
            self.midmove = True
        if value == 1 and self.midmove == True and self.movecount<10:
            self.movecount += 1
            self.midmove = False
            self.retranslatesmallflowers()
        if value > 90:
            value = 90
        canpath = "../../../../Work/HCARD/Images/WateringCan/Can%04d.png" % (value)
        # print canpath
        self.Can.setPixmap(QPixmap(canpath))


    def retranslatesmallflowers(self):
        for i in range(0,self.movecount):
            self.smallflowerlist[i].setPixmap(QPixmap("../../../../Work/HCARD/Images/Assets/FlowerSymbolONAsset 2.png"))
        self.flowerval = 0
        self.retranslateFlower(1)


class Exercise2Widget(QWidget, Exercise2.Ui_Form):
    def __init__(self, parent=None):
        super(Exercise2Widget, self).__init__(parent)
        self.setupUi(self)
        self.angle = 0
        self.targetAngle = 90
        self.countval = 0
        self.most_recent = 0
        self.horizontalSlider.valueChanged.connect(self.leg)

        print 'ex 2 init'
        self.timer = QTimer()
        self.timer.timeout.connect(self.serial_control)
        self.timer.start(100)

    def serial_control(self):
        self.angle = Serial.Serial_read()
        if self.angle == 999:
            self.angle = self.most_recent
        # print self.angle
        self.retranslateLeg(self.angle)
        self.most_recent = self.angle

        # if self.targetAngle+5 >self.angle and self.angle>self.targetAngle-5 and self.count <100:
        #     self.count +=1
        #     # self.flower(self.flowerval)
        # elif self.count > 100:
        #     print 'hold complete'

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
        self.exercise_list = Data.loadObjects('Data_backend.txt')
        datelist = []
        anglelist = []

        for i in self.exercise_list:
            datelist.append(str(i.Date))
            anglelist.append(int(i.Target_A))



        weeks = Data_target.week_list
        Tangles = Data_target.angle_list

        datetime_first = datetime.datetime.strptime(datelist[0], '%Y%m%d')

        for i in range(0,len(weeks)):
            weeks[i] = datetime_first + datetime.timedelta(weeks=int(weeks[i]))
            weeks[i] = int(weeks[i].strftime('%Y%m%d'))

        for i in range(0,len(datelist)):
            datelist[i] = int(datelist[i])

        print weeks , Tangles
        # points = 100
        # X = range(0,points)
        # Y = np.exp2(X)
        #
        self.Plot.plot(weeks,Tangles, pen=(10), symbolBrush=(237, 177, 32), symbolPen='w', symbol='o',symbolSize=5, name="symbol='star'")
        self.Plot.plot(datelist, anglelist, pen=(237, 177, 32), symbolBrush=(237, 177, 32), symbolPen='w', symbol='star', symbolSize=20, name="symbol='star'")


        # self.Plot.plot(X2, Y2, pen=(255, 255, 255), symbolBrush=(237, 177, 32), symbolPen='w', symbol='star', symbolSize=20,
        #                name="symbol='star'")
        # self.Plot.plot(X, Y, pen=(237, 177, 32), symbolBrush=(237, 177, 32), symbolPen='w', symbol='star', symbolSize=20,
        #                name="symbol='star'")

app = QApplication(sys.argv)
form = MainWindow()
#form.setFocus()
form.show()
app.exec_()
