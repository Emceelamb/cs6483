#!/usr/bin/python3

#import socket module

from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a server socket

# Fill in Start

# Fill in end

while True:
    #Establish the conn

    print 'Ready to serve...'

    connectionSocket, addr = # fill in 

    try:
        message = # fill in

        filename = message.split()[1]
        f = open(filename[1:])

        outputdata = # fill

        # send on http header line into socket

        # fill in start
        
        # fil end

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()

    except IOError:
        # send in resp message for file not found

        # fill in start
        # fill in end

        # close client socket

        # fill in start
        
        #fill in end
