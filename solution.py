# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  #Prepare a server socket
  host = "127.0.0.1"
  serverSocket.bind((host, port))
  serverSocket.listen(5)

  while True:
    #Establish the connection
    #print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:

      try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        
        #Send one HTTP header line into socket.
        connectionSocket.send('\nHTTP/1. x 200 OK\n')
        

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
          connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
      except IOError:
        # Send response message for file not found (404)
        connectionSocket.send('\n404 File Not Found\n')

        #Close client socket
        connectionSocket.close()

        

    except (ConnectionResetError, BrokenPipeError):
      pass

  serverSocket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(4001)