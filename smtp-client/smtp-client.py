#!/usr/bin/env python3

from socket import *
import ssl
import base64

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver

mailserver = 'smtp.gmail.com'
#mailserver = 'smtp.dreamhost.com'
PORT = 465
# Create socket called clientSocket and establish a TCP connection with mailserver

clientSocket = socket(AF_INET, SOCK_STREAM)

# ssl
ssl_version=ssl.PROTOCOL_TLSv1
clientSocket = ssl.wrap_socket(clientSocket);

clientSocket.connect((mailserver, PORT))


recv = clientSocket.recv(1024).decode()

if recv[:3] != '220':
    print('220 reply not received from server. 1')

# Send HELO command and print server response.

heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server. 2')

# auth
username = "ml.test.emailer.123@gmail.com"
password = "v3rystr0ng"
base64_str = ("\x00"+username+"\x00"+password).encode()
base64_str = base64.b64encode(base64_str)
authMsg = "AUTH PLAIN ".encode()+base64_str+"\r\n".encode()
clientSocket.send(authMsg)
recv_auth = clientSocket.recv(1024)
print(recv_auth.decode())

print("Authenticated")

# MAIL FROM
clientSocket.send('MAIL FROM: <ml.test.emailer.123@gmail.com>\r\n'.encode())
recv1 = clientSocket.recv(1024)

if recv1[:3] != b'250':
    print(recv1[:3],'250 reply not received 3')
else:
    print("mail from OK")

# Send RCPT TO command and print server response. 
clientSocket.send('RCPT TO: <marktranquilizerlam@gmail.com>\r\n'.encode())
recv1 = clientSocket.recv(1024)
print (recv1)
if recv1[:3] != b'250':
    print('250 reply not received 4')
else: 
    print("mail to ok")

# Send DATA command and print server response. 

data = "DATA\r\n"
clientSocket.send(data.encode())
recv1 = clientSocket.recv(1024)
recv1 = recv1.decode()

if recv1[:3] != b'354':
    print('Ok reply not received. instead got ', recv1)
else: 
    print("Data ok")


# Make subject
subject = "Subject: Sent by python\r\n\r\n"
clientSocket.send(subject.encode())

# Send msg
clientSocket.send(msg.encode())

# Send message data.
clientSocket.send(endmsg.encode())
recv1 = clientSocket.recv(1024)
print (recv1)
if recv1[:3] != b'250':
    print('250 reply not received 5')
else:
    print("mail ok")

# Send QUIT command and get server response.
clientSocket.send(b'QUIT\r\n')
clientSocket.close();
print("Message sent!")
