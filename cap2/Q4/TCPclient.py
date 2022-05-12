from socket import *
import sys

serverPort = 12000

nArg = len(sys.argv)
if nArg < 3:
    print('Uso: TCPClient.py N x.x.x.x\n')
    sys.exit()


serverName = sys.argv[2]
natNum = int(sys.argv[1])
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
    
for i in range(0,natNum+1):
    clientSocket.send(str(i).encode())
    modifiedSentence = clientSocket.recv(1024)
    print('Response: ', modifiedSentence.decode())
clientSocket.close()
