import serial
# import serial.tools.list_ports
# ports = list(serial.tools.list_ports.comports())
# for p in ports:

    # print p
ser = serial.Serial('COM10', 115200, timeout=0)
while True:
    print ser.readline()