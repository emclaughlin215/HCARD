import serial

ser = serial.Serial('COM12', 115200)

while True:
    print ser.readline()
    ser.write('back')
    ser.writt('front')