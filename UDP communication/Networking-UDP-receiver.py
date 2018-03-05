import socket

UDP_IP = "146.169.211.210."
UDP_PORT = 5002
data="" # declare for the while loop

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while data != "exit":
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data, "\n"

sock.close()