import sys
import socket
import select
import time

host = "localhost"
port = 9009

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try :
    s.connect((host, port))
except :
    print('Unable to connect')
    sys.exit()

print('Connected to remote host.')

#Try to send something
#message = b"Test connection send from client!"
message = "Test connection send from client!"
#s.send(message)
#s.send(str(message))
s.send(bytes(message, 'UTF-8'))

#Receive message
incomming_byte_message = s.recv(4096)
print("Recieved: " + incomming_byte_message.decode('utf-8'))

#Close sockets
s.shutdown(socket.SHUT_RDWR)
s.close()
