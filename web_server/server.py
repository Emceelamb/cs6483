#!/usr/bin/env python3
 #import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverPort = 8000
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('Server is up on port '+str(serverPort))
#Fill in end
while True:
#Establish the connection
     #Fill in start
    connectionSocket, addr = serverSocket.accept()
    print('Ready to serve...')
     #Fill in entry:
    try:
        message = connectionSocket.recv(1024)
         #Fill in start
         #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        toSendData=b''
        f.close()
         #Fill in end
        #Send one HTTP header line into socket
        #Fill in start
        #Fill in end
        #Send the content of the requested file to the client
        print(outputdata)
        # connectionSocket.send('\nHTTP/1.1 200 OK\n'.encode())
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode()) 
        # for i in range(0, len(outputdata)):
        #     toSendData=toSendData + bytes(outputdata[i], encoding='utf-8')
        #     toSendData=toSendData+(bytes(outputdata[i], encoding='utf-8'))
        #     connectionSocket.send(bytes(outputdata[i], encoding='utf-8'))
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        # print(toSendData)
        # connectionSocket.send(outputdata)
        connectionSocket.send("\r\n".encode())
        # connectionSocket.send(b'\nblah\n')
        # connectionSocket.send(b"\r\n")
        connectionSocket.close()
        print('File received')
    except IOError:
        print('ERR: File not found.')
        connectionSocket.send(b'\n404 File Not Found\n')
        connectionSocket.close()

connectionSocket.close()        
serverSocket.close()
sys.exit()

