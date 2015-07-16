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

def check_for_incoming_data(server_socket, planet_list):
    #Check that the server_socket has a valid file descriptor
    if server_socket.fileno() != -1:
        #Use select to check if there is anything to read, using timeout value 0
        ready_to_read, ready_to_write, in_errror = select.select([server_socket], [], [], 0)

        #Check if ready_to_read contains anything
        if len(ready_to_read) > 0:
            #Extract message
            incoming_byte_message = ready_to_read[0].recv(buffer_length)   #Buffer_length is a global variable

            if incoming_byte_message:
                #Decode message
                message = incoming_byte_message.decode("UTF-8")
                print("Received: " + message)
                return message

            else:
                print("Connection dropped.")
    #Nothing received, return the same old list
    return planet_list

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

    #Create empty list of planets
    list_of_planets = []

    while run_client_loop:
        #Check for incoming data
        list_of_planets = check_for_incoming_data(server, list_of_planets)

        #Clear screen
        screen.fill((0,0,0))

        #Draw planets
        if len(list_of_planets) > 0:
            for planet in list_of_planets:
                #bom.position = b[0]
                #bom.radius   = b[1]
                print(planet[0]["x"])
                print(planet[0]["y"])
                print(planet[1])
                pygame.draw.circle(screen,(255,0,255),(int(planet[0]["x"]), int(planet[0]['y'])), int(planet[1]), 0)

        #Handle events

        #Update screen
        pygame.display.flip()

        #run_client_loop = False

    #Handle end of program
    server.close()
    pygame.quit()







