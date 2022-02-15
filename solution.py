# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
#Socket()
  serverSocket = socket(AF_INET, SOCK_STREAM)
  #Prepare a TCP server socket bind()
  serverSocket.bind(("", port))
  #Fill in start
  serverSocket.listen(1)
  #print("The server is ready to receive")
  #Fill in end

  while True:
    #Establish the connection
    #print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:

      try:
        message = connectionSocket.recv(1024)
        file = message.split()[1]
        filename = file[1:]
        f = open(filename[1:])
        outputdata = f.read()
        f.close()

        #Send one HTTP header line into socket.
        #Fill in start
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        connectionSocket.send("Content-Length: {}\r\n".format(len(outputdata)).encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send("\r\n".encode()
        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
          connectionSocket.send(outputdata[i].encode()
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
      except IOError:
        # Send response message for file not found (404)
        #Fill in start
        connectionSocket.send("HTTP/1.1 400 ERROR: File Not Found\r\n".encode())
        #Fill in end


        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end

    except (ConnectionResetError, BrokenPipeError):
      pass

  serverSocket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)