import sys
import socket
import select
import time

host = "localhost"
port = 9009

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try :
    s.bind((host, port))
except :
    print('Unable to bind')
    sys.exit()

try :
    s.listen(5)
except :
    print('Unable to listen')
    sys.exit()

#Accept connection
(clientsocket, address) = s.accept()

#Receive message
incomming_byte_message = clientsocket.recv(4096)

print("Received: " + incomming_byte_message.decode('utf-8'))

#Send message
message = "Hello there, I got your message! Kan du höra mig?"
clientsocket.send(bytes(message, "UTF-8"))

#clientsocket.shutdown(socket.SHUT_RDWR)
clientsocket.close()
#s.shutdown(socket.SHUT_RDWR)
s.close()
