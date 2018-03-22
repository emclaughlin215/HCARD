import matplotlib.pyplot as plt
import os.path
import time
import glob
import shutil
import os

class Exercises:
    def __init__(self , Date= '' , Target_A = '' , Duration_hold = '' , Score = '' , Comment = '' , Advice = ''):
        self.Date = Date
        self.Target_A = Target_A
        self.Duration_hold = Duration_hold
        self.Score = Score
        self.Comment = Comment
        self.Advice = Advice

    def writeToFile(self, file):
        file.write(self.Date)
        file.write("\n")
        file.write(self.Target_A)
        file.write("\n")
        file.write(self.Duration_hold)
        file.write("\n")
        file.write(self.Score)
        file.write("\n")
        file.write(self.Comment)
        file.write("\n")
        file.write(self.Advice)
        file.write("\n")


    def readFromFile(self, file):
        self.Date = file.readline().rstrip('\n')
        self.Target_A = file.readline().rstrip('\n')
        self.Duration_hold = file.readline().rstrip('\n')
        self.Score = file.readline().rstrip('\n')
        self.Comment = file.readline().rstrip('\n')
        self.Advice = file.readline().rstrip('\n')



def saveObject(filename, object):
    file = open(filename, 'a')  ## w means write
    object.writeToFile(file)

def NumLines(filename):
    file = open(filename, 'r')
    with file as f:
        return sum(1 for _ in f)

def loadObjects(filename):
    file = open(filename, 'r')
    numobj = (NumLines(filename))/6
    objlist = []

    for el in range(0, numobj):
        instance = Exercises()
        instance.readFromFile(file)
        objlist.append(instance)
    file.close()
    return objlist