
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def ser():
    print 'hello'

timer = QTimer()
timer.timeout()
timer.timeout.connect(ser())
timer.start(1000)

