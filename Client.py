#IPBM Client

#IPBM
#import PlaySpace
#import MissileLauncher
#import BodyOfMass

#Network
import socket
import select

#Other
import time
import os
import sys
import math
import pygame

#Define receive buffer length
buffer_length = 4096

def check_for_incoming_data(server_socket):
    #Check that the server_socket has a valid file descriptor
    if server_socket.fileno() == -1:
        #Broken connection
        return []

    #Use select to check if there is anything to read, using timeout value 0
    ready_to_read, ready_to_write, in_errror = select.select([server_socket], [], [], 0)

    #Check if ready_to_read contains anything
    if len(ready_to_read) > 0:
        #Extract message
        incoming_byte_message = ready_to_read[0].recv(buffer_length)   #Buffer_length is a global variable
        print("Received: " + incoming_byte_message.decode("UTF-8"))

        #Decode message
        message = incoming_byte_message.decode("UTF-8")

    return []

if __name__ == "__main__":
    #Check command line arguments
    if(len(sys.argv) < 3) :
        print("Usage : Python Client.py ServerNameOrIp Port")
        sys.exit()
    server_name = sys.argv[1]
    server_port = int(sys.argv[2])

    #Connect to server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try :
        server.connect((server_name, server_port))
    except :
        print("Unable to connect to server: " + server_name)
        sys.exit()
    print("Connected to remote host: " + server_name)

    #Create window and display it
    (win_x, win_y) = (640, 480)
    screen = pygame.display.set_mode((win_x,win_y))
    pygame.display.set_caption("A primitive Client")
    pygame.display.flip()

    #Create client loop control variable
    run_client_loop = True

    while run_client_loop:
        #Check for incoming data
        check_for_incoming_data(server)

        #Clear screen

        #Draw planets

        #Handle events

        run_client_loop = False

    #Handle end of program
    server.close()
    pygame.quit()







