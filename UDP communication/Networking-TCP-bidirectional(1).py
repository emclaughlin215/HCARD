import socket

def chat(connection, listen):
    MESSAGE = "" # Declare message variable outside of the loop so we can conditionally exit
    while MESSAGE != 'exit': # Keep going until we either type in or receive an exit message
        if listen == 0: # If we are the sender start with writing the message
            MESSAGE = raw_input("Please enter your message (write exit to terminate) \n") # prompt user to input a message
            connection.send(MESSAGE) # Transmit it
            if MESSAGE == 'exit': # break after sending and do not wait for the reply
                break
        MESSAGE = connection.recv(BUFFER_SIZE) # Wait to get the data
        print "Message received:\n", MESSAGE # and then print it
        listen = 0 # if we were in the listening mode, switch to transmission
    print "Closing connection..."
    connection.close() # Do not forget to clean up the connection or the port will be blocked until system restart

print("Starting...")
ROLE = "SEND" # LISTEN or SEND
#ROLE = "LISTEN" # LISTEN or SEND

TCP_IP = '147.169.133.126'  # IP to connect to if we are the sender
TCP_IP_LISTEN = '0.0.0.0' # IP to listen on (0.0.0.0 will listen to any source IP)
TCP_PORT = 631 # Port
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, # Internet socket
                  socket.SOCK_STREAM) # with TCP protocol

print "Role... ", ROLE
if ROLE == "SEND":
    try:
        print "Trying to connect to ", TCP_IP, " : ", TCP_PORT
        #s.settimeout(2) # set timeout to ... second, if we can't connect we will raise an exception
        s.connect((TCP_IP, TCP_PORT)) # attempt to establish the connection
        print "Yay Connected!!!!"
        chat(s,0) # remember 0 stands for the role of sender
    except Exception as e: # handle errors
        print "Socket failed with error: ", e
    finally:
        s.close()

if ROLE == "LISTEN":
    try:
        s.bind((TCP_IP_LISTEN, TCP_PORT)) # bind the socket
        s.listen(1) # and switch it to listening mode
        conn, addr = s.accept() # wait for incoming connection
        print 'Established connection with address:', addr
        chat(conn, 1) # once connection has been established - start the console chat
    except Exception as e:
        print "Connection failed with error: ", e
    finally:
        conn.close()

print "Exiting..."