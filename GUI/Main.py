# from PySide.QtCore import *
# from PySide.QtGui import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import time
import numpy as np
import pyqtgraph as pg
import datetime
import math
import serial

import Exercise0, Exercise1, Exercise2, Exercise3 ,Home, Results1, Data_target, Data, Email
import sys
import serial
import testblank

Selected_ex = 1
Selected_ex_angle = 0
Last_exercise_list =[0,0,0,0,0,0,0,0,0,0]

port = 'COM13'
try:
    ser = serial.Serial(port, 115200)
    print 'board connected'
except:
    ser = None
    print 'no board connected'



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
        Results_Widget = ResultsWidget(self)
        self.central_widget.addWidget(Results_Widget)
        self.central_widget.setCurrentWidget(Results_Widget)
        Results_Widget.Home_button.mousePressEvent = self.Home

    def Exercise0(self,val):
        Exercise0_Widget = Exercise0Widget(self)
        self.central_widget.addWidget(Exercise0_Widget)
        self.central_widget.setCurrentWidget(Exercise0_Widget)

        Exercise0_Widget.Home_button.mousePressEvent = self.Home
        Exercise0_Widget.Go_button_2.mousePressEvent = self.Exercise1
        Exercise0_Widget.Ex_angle.mousePressEvent = self.Exercise1


    def Exercise1(self,val):
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
        Exercise_Widget.Ex_complete.mousePressEvent = self.PostExercise

    def PostExercise(self,val):
        Post_ex_Widget = PostExerciseWidget(self)
        self.central_widget.addWidget(Post_ex_Widget)
        self.central_widget.setCurrentWidget(Post_ex_Widget)
        Post_ex_Widget.pushButton.clicked.connect(self.Home)
        # Post_ex_Widget.saveButton.mousePressEvent = self.Home


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
        percentage = int(selected_ex_angle)*100/135
        self.progressBar.setProperty("value", percentage)
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
            self.Tab_1.setPixmap(QPixmap("Graphics/Assets/ResultsLogoAsset 9.png"))
            self.Tab_2.setPixmap(QPixmap("Graphics/Assets/ResultsLogoAsset 10.png"))
            self.Tab_3.setPixmap(QPixmap("Graphics/Assets/ResultsLogoAsset 10.png"))
            self.Exercise_box.setPixmap(QPixmap("Graphics/Assets/SelectedExerciseBox 1.png"))
        elif tab_clicked == 2:
            self.Tab_2.setPixmap(QPixmap("Graphics/Assets/ResultsLogoAsset 9.png"))
            self.Tab_1.setPixmap(QPixmap("Graphics/Assets/ResultsLogoAsset 10.png"))
            self.Tab_3.setPixmap(QPixmap("Graphics/Assets/ResultsLogoAsset 10.png"))
            self.Exercise_box.setPixmap(QPixmap("Graphics/Assets/SelectedExerciseBox 2.png"))

        elif tab_clicked == 3:
            self.Tab_3.setPixmap(QPixmap("Graphics/Assets/ResultsLogoAsset 9.png"))
            self.Tab_2.setPixmap(QPixmap("Graphics/Assets/ResultsLogoAsset 10.png"))
            self.Tab_1.setPixmap(QPixmap("Graphics/Assets/ResultsLogoAsset 10.png"))
            self.Exercise_box.setPixmap(QPixmap("Graphics/Assets/SelectedExerciseBox.png"))

class Exercise1Widget(QWidget, Exercise1.Ui_Form):
    def __init__(self, parent=None):
        super(Exercise1Widget, self).__init__(parent)
        self.setupUi(self)

        ## obtaining target angle
        global selected_ex_angle
        self.targetAngle = selected_ex_angle
        self.Target_angle.setText(str(self.targetAngle))
        ## serial connect check
        global ser
        try:
            if ser == None or ser.isOpen == False:
                ser = serial.Serial(port, 115200)
                print 'reconnecting to device'

            ## send target angle to initialise
            # if ser.readline()== None:
            ser.write(str(self.targetAngle))
            print 'sent angle'
        except:
            a = 'no board'

        self.horizontalSlider.valueChanged.connect(self.pot)

        self.flowerval = 1
        self.midmove = False
        self.movecount = 0
        self.smallflowerlist = [self.Flower_small_1,self.Flower_small_2,self.Flower_small_3,self.Flower_small_4,self.Flower_small_5,self.Flower_small_6,self.Flower_small_7,self.Flower_small_8,self.Flower_small_9,self.Flower_small_10]

        self.horizontalSlider_2.valueChanged.connect(self.retranslateFlower)
        self.timer = QTimer()
        self.timer.timeout.connect(self.serial_control)
        self.timer.start(1)

    def serial_control(self):
        try:
            self.angle = ser.readline()
            print self.angle
            try:
                self.angle = float(self.angle)
                self.angle = int(self.angle)
            except(ValueError):
                return (self.angle)
            if type(self.angle) == int:
                self.retranslatePot(self.angle)  # replace with self.pot(self.angle)
            else:
                print(self.angle, "not int")
            self.Current_angle.setText(str(self.angle))
            if (self.targetAngle+2>self.angle>self.targetAngle-2) and self.flowerval <400:
                self.flowerval +=1
                self.retranslateFlower(self.flowerval)
        except:
            a = 'no board'

    def pot(self, value): ## actually i mean can, changes the watering can image
        # print (value)
        self.retranslatePot(value)
        ### if watering can angle at target, adds to the flower size (flowerval)
        if (value > self.targetAngle-5) and (value< self.targetAngle+5) and self.flowerval <400 and self.movecount <10:
            self.flowerval +=1
            self.retranslateFlower(self.flowerval)

    def retranslateFlower(self, value):
        flowerpath = "Graphics/FlowerGrowing/AnimationFlowers%04d.png" % (value)
        print flowerpath
        self.Flower.setPixmap(QPixmap(flowerpath))

    def retranslatePot(self, value):
        # print self.movecount
        # print self.midmove
        # print value
        self.Current_angle.setText(str(value))
        if value > 10:
            self.midmove = True
        if value < 10 and  self.midmove == True and self.movecount<10:
            global Last_exercise_list
            Last_exercise_list[self.movecount] = self.flowerval
            self.movecount += 1
            self.midmove = False
            self.retranslatesmallflowers()
        if value > 90:
            value = 90
        canpath = "Graphics/WateringCan/Can%04d.png" % (value)
        # print canpath
        self.Can.setPixmap(QPixmap(canpath))
        if self.movecount == 10:
            self.Ex_complete.setGeometry(QRect(180, 100, 331, 201))
            self.timer.stop()


    def retranslatesmallflowers(self):
        for i in range(0,self.movecount):
            self.smallflowerlist[i].setPixmap(QPixmap("Graphics/Assets/FlowerSymbolONAsset 2.png"))
        self.flowerval = 0
        self.retranslateFlower(1)

class Exercise2Widget(QWidget, Exercise2.Ui_Form):  ## still need to count movements and move ex done label
    def __init__(self, parent=None):
        super(Exercise2Widget, self).__init__(parent)
        self.setupUi(self)

        ## obtain target angle
        global selected_ex_angle
        self.targetAngle = selected_ex_angle
        self.Target_angle.setText(str(self.targetAngle))
        self.angle = 0
        print self.targetAngle
        ## serial connect check
        global ser
        try:
            if ser == None or ser.isOpen == False:
                ser = serial.Serial(port, 115200)
                print 'reconnecting to device'

            ## send target angle to initialise
            # if ser.readline()== None:
            ser.write(str(self.targetAngle))
            print 'sent angle'
        except:
            print 'no board'

        self.midmove = False
        self.movecount = 0
        self.countval = 0
        self.smalltargetlist = [self.Targetsmall, self.Targetsmall_2, self.Targetsmall_3, self.Targetsmall_4,
                                self.Targetsmall_6, self.Targetsmall_7, self.Targetsmall_5, self.Targetsmall_8,
                                self.Targetsmall_9, self.Targetsmall_10]

        self.most_recent = 0
        self.horizontalSlider.valueChanged.connect(self.leg)
        self.horizontalSlider_2.valueChanged.connect(self.moveTarget)

        self.moveTarget(self.targetAngle)

        self.timer = QTimer()
        self.timer.timeout.connect(self.serial_control)
        self.timer.start(1)

    def moveTarget(self, val):
        R = 200
        xk = 350
        yk = 100
        x = xk + R * math.sin(math.radians(90-val))
        x = int(x)
        y = yk + R * math.cos(math.radians(90-val))
        y = int(y)
        self.Target.setGeometry(QRect(x,y, 100, 100))
        self.targetAngle = val
        # print(x , y , val)

    def growTargetImage(self):
        self.countval += 1
        if self.countval >400:
            self.countval = 400
        self.retranslateTarget(self.countval)

    def retranslateTarget(self, val):
        TargetPath = "Graphics/Target/Target%04d.png" % (val)
        self.Target.setPixmap(QPixmap(TargetPath))

    def serial_control(self):

        try:
            self.angle = ser.readline()
            print self.angle
            try:
                self.angle = float(self.angle)
                self.angle = int(self.angle)
            except(ValueError):
                return (self.angle)
            if type(self.angle) == int:
                if self.angle == 999:
                    print 'HIPFAIL'
                    self.showhipfail()
                    print self.angle
                else:
                    self.retranslateLeg(self.angle)  # replace with self.pot(self.angle)
                    # self.Leg_warning.setGeometry(QRect(1000, 1000, 221, 41))
            else:
                print(self.angle, "not int")
        except:
            a = 'no board'
    def showhipfail(self):
        self.Leg_warning.setGeometry(QRect(120, 100, 221, 41))
        hiptime = QTimer()
        hiptime.singleShot(500, self.hidehipfail)
    def hidehipfail(self):
        self.Leg_warning.setGeometry(QRect(1000, 1000, 221, 41))

    def leg(self,val):
        self.angle = self.horizontalSlider.value()
        print self.angle
        self.retranslateLeg(self.angle)

    def retranslatesmalltarget(self):
        for i in range(0,self.movecount):
            self.smalltargetlist[i].setPixmap(QPixmap("Graphics/Assets/Targetlogo.png"))
        self.countval = 0
        self.retranslateTarget(1)

    def retranslateLeg(self, value):
        legpath = "Graphics/LegMovement/LegMove%04d.png" % (135-value)
        # print legpath
        self.Leg.setPixmap(QPixmap(legpath))
        # print value, self.targetAngle
        self.Current_angle.setText(str(value))
        if self.angle > self.targetAngle-2 and self.angle < self.targetAngle+2 :
            self.growTargetImage()
        if value > 10:
            self.midmove = True
        if value < 10 and self.midmove == True and self.movecount<10:
            global Last_exercise_list
            Last_exercise_list[self.movecount] = self.countval
            self.movecount += 1
            self.midmove = False
            self.retranslatesmalltarget()
        if self.movecount == 10:
            self.Ex_complete.setGeometry(QRect(180, 100, 331, 201))
            self.timer.stop()

class PostExerciseWidget(QWidget, Exercise3.Ui_Form):
    def __init__(self, parent=None):
        super(PostExerciseWidget, self).__init__(parent)
        self.setupUi(self)
        self.saveButton.mousePressEvent = self.save

        small_image_list = [self.Small_image_1,self.Small_image_2,self.Small_image_3,self.Small_image_4,self.Small_image_5, self.Small_image_6, self.Small_image_7, self.Small_image_8, self.Small_image_9, self.Small_image_10]
        global Selected_ex
        global Last_exercise_list
        global selected_ex_angle

        print 'Selected_ex_angle', selected_ex_angle

        ## define score, angle and Advice
        self.targetAngle = str(selected_ex_angle)
        self.holdDuration = np.average(Last_exercise_list)
        if self.holdDuration < 120:
            self.Score = 1
        elif self.holdDuration < 240:
            self.Score = 2
        elif self.holdDuration < 400:
            self.Score = 3
        if self.Score == 1:
            self.Advice = 'Try holding for a bit longer'
        elif self.Score == 2:
            self.Advice = 'Nearly there! Try holding the position just a little longer!'
        elif self.Score == 3:
            self.Advice = 'Keep it up!'

        ## initialise graphics on page
        starlist = [self.Star_1, self.Star_2, self.Star_3]
        for i in range(0,self.Score):
            print i
            starlist[i].setPixmap(QPixmap("Graphics/Assets/Star_largeAsset 1.png"))

        last_angle_string = "%s degrees" %(self.targetAngle)
        print last_angle_string
        self.Last_angle.setText(last_angle_string)
        percentage = int(selected_ex_angle) * 100 / 135
        self.progressBar.setProperty("value", percentage)
        self.advice_label.setText(self.Advice)

        # retranslate small icons
        if Selected_ex == 1:
            for i in range(0,10):
                print i,Last_exercise_list[i]
                TargetPath = "Graphics/FlowerGrowingSmall/AnimationFlowers%04d.png" % (Last_exercise_list[i])
                print TargetPath
                small_image_list[i].setPixmap(QPixmap(TargetPath))
        if Selected_ex == 2:
            for i in range(0,10):
                print Last_exercise_list[i]
                TargetPath = "Graphics\Targetsmall\Targetsmall%04d.png" % (Last_exercise_list[i])
                small_image_list[i].setPixmap(QPixmap(TargetPath))

    def save(self,val):
        print 'saving'
        print self.comment.text()
        if self.comment.text() != "Type your comment here..." and self.comment.text() != '':
            currentDate = str(time.strftime("%Y%m%d"))
            # global Selected_ex_angle
            global Last_exercise_list
            # targetAngle = str(Selected_ex_angle)
            # holdDuration = str(np.average(Last_exercise_list))
            # print holdDuration
            # Score = 1
            # if holdDuration< 120:
            #     Score = 1
            # elif holdDuration <240:
            #     Score =2
            # elif holdDuration <400:
            #     Score = 3
            Comment = str(self.comment.text())
            # if Score == 1:
            #     Advice = 'Try holding for a bit longer'
            # elif Score == 2:
            #     Advice = 'Nearly there! Try holding the position just a little longer!'
            # elif Score == 3:
            #     Advice = 'Keep it up!'
            self.Score = str(self.Score)
            self.holdDuration = str(self.holdDuration)
            # print currentDate, type(currentDate), self.targetAngle, type(targetAngle), holdDuration, type(holdDuration),Score, type(Score), Comment, type(Comment),Advice, type(Advice)
            new_object = Data.Exercises(currentDate,self.targetAngle,self.holdDuration,self.Score,Comment,self.Advice)
            Data.saveObject('Data_backend.txt',new_object)
            self.pushButton.click()
            Email.send_email()
        else:
            QMessageBox.about(self, "ERROR", "Please leave a comment")

class ResultsWidget(QWidget , Results1.Ui_Form):
    def __init__(self, parent=None):
        pg.setConfigOption('background', 'w')
        super(ResultsWidget, self).__init__(parent)
        self.setupUi(self)
        self.exercise_list = Data.loadObjects('Data_backend.txt')
        self.most_recent_angle = self.exercise_list[-1].Target_A
        self.Current_angle.setText(str(self.most_recent_angle))
        self.proggression_percent = str(int(self.most_recent_angle)*100/135)
        self.Current_progression.setText(self.proggression_percent)

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

        # points = 100
        # X = range(0,points)
        # Y = np.exp2(X)
        #
        self.Plot.plot(weeks,Tangles, pen=(53, 168, 224), symbolBrush=(53, 168, 224), symbolPen='w', symbol='o',symbolSize=5, name="symbol='star'")
        self.Plot.plot(datelist, anglelist, pen=(248, 177, 51), symbolBrush=(248, 177, 51), symbolPen='w', symbol='star', symbolSize=20, name="symbol='star'")


        # self.Plot.plot(X2, Y2, pen=(255, 255, 255), symbolBrush=(237, 177, 32), symbolPen='w', symbol='star', symbolSize=20,
        #                name="symbol='star'")
        # self.Plot.plot(X, Y, pen=(237, 177, 32), symbolBrush=(237, 177, 32), symbolPen='w', symbol='star', symbolSize=20,
        #                name="symbol='star'")

app = QApplication(sys.argv)
form = MainWindow()
#form.setFocus()
form.show()
app.exec_()
