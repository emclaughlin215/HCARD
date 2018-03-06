import socket

UDP_IP = "127.0.0.1"  # This is localhost address for same-machine testing comment this line if working in pairs
#UDP_IP = "147.169.133.126" # configure this with the other computer's IP and uncomment
UDP_PORT = 5001
MESSAGE = "Hello, Jacob, Love Kind David!"
#MESSAGE = "exit" # Using this message will terminate the UDP receiver

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
             socket.SOCK_DGRAM) # UDP
bytesSent = sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

print "We have just sent ", bytesSent, " bytes!"

sock.close()