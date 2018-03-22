# //This code prints the serial communication
import serial
import random
# //For Davids MBP:/dev/cu.usbmodem1441
# //Change to port
global mostrecent
try:
    ser = serial.Serial('COM13', 115200)
except:
    print 'no serial device'

def Serial_read():
    stringval = ser.readline()

    try:
        stringval = float(stringval)
        angle = int(stringval)
        return(angle)
    except(ValueError):
        return (stringval)

def Serial_write(val):
    ser.write(val)


# def Serial_read():
#     randval = random.randrange(-90,90)
#     stringval = "The current angle of the device is:%2d" %(randval)
#     angle = int(stringval[35:])
#     if angle<0:
#         angle = abs(angle)
#     else:
#         angle = angle+90
#     return(angle)

