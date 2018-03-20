# //This code prints the serial communication
import serial
import random
# //For Davids MBP:/dev/cu.usbmodem1441
# //Change to port
global mostrecent


def Serial_read():
    ser = serial.Serial('COM13', 115200)
    stringval = ser.readline()
    # print(stringval)

    try:
        stringval = float(stringval[:-2])
        angle = int(stringval)
        if angle<0:
            angle = 90 + abs(angle)
        else:
            angle = 90 - angle
        return(angle)
    except(ValueError):
        print ' error'
        return (999)



# def Serial_read():
#     randval = random.randrange(-90,90)
#     stringval = "The current angle of the device is:%2d" %(randval)
#     angle = int(stringval[35:])
#     if angle<0:
#         angle = abs(angle)
#     else:
#         angle = angle+90
#     return(angle)

