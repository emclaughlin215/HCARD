# //This code prints the serial communication
import serial
#
# //For Davids MBP:/dev/cu.usbmodem1441
# //Change to port

def Serial_read():
    ser = serial.Serial('COM12', 115200)
    return ser.readline()








