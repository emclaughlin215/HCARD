<<<<<<< HEAD
# This code prints the serial communication
=======
# //This code prints the serial communication
>>>>>>> f1a0b26979e682741c05e95a4bcb085a3e8a40c6
import serial
#
# //For Davids MBP:/dev/cu.usbmodem1441
# //Change to port

def Serial_read():
    ser = serial.Serial('COM12', 115200)
    return ser.readline()


<<<<<<< HEAD
# For Davids MBP:/dev/cu.usbmodem1441
# Change to port
ser = serial.Serial('/dev/cu.usbmodem1441', 115200)
while True:
    print ser.readline()
=======
>>>>>>> f1a0b26979e682741c05e95a4bcb085a3e8a40c6






