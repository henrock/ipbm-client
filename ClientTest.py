# chat_client.py

import sys
import socket
import select
import time

def chat_client():
    if(len(sys.argv) < 4) :
        print('Usage : python chat_client.py hostname port client_number')
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.settimeout(2)

    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print('Unable to connect')
        sys.exit()

    print('Connected to remote host.')

    #Time variables
    start_time      = time.time()
    last_send       = time.time()
    current_time    = time.time()
    elapsed_time    = 0

    #Counter
    counter = 1

    while elapsed_time < 10:
        #Update time
        current_time = time.time()
        elapsed_time = current_time - start_time
        #counter += 1

        #Check status of sockets
        socket_list = [s]
        ready_to_read,ready_to_write,in_error = select.select(socket_list , socket_list, [])

        #Check for messages
        for sock in ready_to_read:
            if sock == s:
                # incoming message from remote server, s
                incomming_byte_message = sock.recv(4096)
                print("Recieved: " + incomming_byte_message.decode('utf-8'))


        #Send messages every 2 seconds
        if current_time - last_send > 2:
            for sock in ready_to_write:
                message_string = "Client " + str(sys.argv[3]) + " message number: " + str(counter)
                byte_message = message_string.encode('utf-8')
                sock.send(byte_message)
                #print("Recieved: "
                print("    Sent: " + message_string)
                last_send = current_time
                counter += 1

        #Wait
        #print("Waiting")
        #time.wait(100)
        #print("Done waiting")
    s.close()


if __name__ == "__main__":

    sys.exit(chat_client())
