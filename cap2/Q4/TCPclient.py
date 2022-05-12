from socket import *
import sys

serverPort = 12000

nArg = len(sys.argv)
if nArg < 2:
    print('Uso: TCPClient.py x.x.x.x\n')
    sys.exit()


serverName = sys.argv[1]
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
    
msg = 'Hello'
while True:
    clientSocket.send(msg.encode())
    response = clientSocket.recv(2048).decode()
    print(response)
    if response.find("Até logo") != -1:
        clientSocket.close()
        break
    msg=input()
