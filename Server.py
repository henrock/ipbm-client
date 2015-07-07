#IPBM Server

#IPBM
#import BodyOfMass

#Pygame
import pygame

#Network
import socket
import select

#Network stuff
host = "localhost"
port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
message = "Hello world!"
#s.sendall(b'Hello, world')
s.sendall(message)
data = s.recv(1024)
s.close()
print('Received', repr(data))
