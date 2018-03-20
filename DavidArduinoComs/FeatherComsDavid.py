# This code prints the serial communication
import serial

# For Davids MBP:/dev/cu.usbmodem1441
# Change to port
ser = serial.Serial('/dev/cu.usbmodem1441', 115200)
while True:
    print ser.readline()






