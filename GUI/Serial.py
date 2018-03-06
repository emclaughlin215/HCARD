# //This code prints the serial communication
import serial
import random
# //For Davids MBP:/dev/cu.usbmodem1441
# //Change to port

# def Serial_read():
#     ser = serial.Serial('COM12', 115200)
#     stringval =  ser.readline()
#      angle = int(stringval[35:])
#     if angle<0:
#         angle = abs(angle)
#     else:
#         angle = angle+90
#     return(angle)

def Serial_read():
    randval = random.randrange(-90,90)
    stringval = "The current angle of the device is:%2d" %(randval)
    angle = int(stringval[35:])
    if angle<0:
        angle = abs(angle)
    else:
        angle = angle+90
    return(angle)

