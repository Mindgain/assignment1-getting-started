#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverPort = 13331 #sets port
host = "127.0.0.1"
serverSocket.bind((host, serverPort))
serverSocket.listen(1)
while True:
    #Establish the connection
    #print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        #print message
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
 #Send one HTTP header line into socket
        connectionSocket.send('\nHTTP/1. x 200 OK\n')
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
        #print \File Received/

    except IOError:
        #Send response message for file not found
        connectionSocket.send('\n404 File Not Found\n')
 #Close client socket
connectionSocket.close()
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data