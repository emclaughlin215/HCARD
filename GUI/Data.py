import matplotlib.pyplot as plt
import os.path
import time
import glob
import shutil
import os

class Puppies:
    def __init__(self , DateTime= '' , Target_A = None , Max_A = None , Duration_hold = None , Score = None , Comment = '' ):
        self.DateTime = DateTime
        self.Target_A = Target_A
        self.Max_A = Max_A
        self.Duration_hold = Duration_hold
        self.Score = Score
        self.Comment = Comment

    def writeToFile(self, file):
        file.write(self.DateTime)
        file.write("\n")
        file.write(self.Target_A)
        file.write("\n")
        file.write(self.Max_A)
        file.write("\n")
        file.write(self.Duration_hold)
        file.write("\n")
        file.write(self.Score)
        file.write("\n")
        file.write(self.Comment)
        file.write("\n")


    def readFromFile(self, file):
        self.DateTime = file.readline().rstrip('\n')
        self.Target_A = file.readline().rstrip('\n')
        self.Max_A = file.readline().rstrip('\n')
        self.Duration_hold = file.readline().rstrip('\n')
        self.Score = file.readline().rstrip('\n')
        self.Comment = file.readline().rstrip('\n')



def saveObject(filename, object):
    file = open(filename, 'a')  ## w means write
    object.writeToFile(file)
