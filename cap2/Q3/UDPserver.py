from socket import *
import _thread

host = ''
serverPort = 12000

def conexao(msg, cli):
    sentence = msg.decode().upper()
    serverSocket.sendto(sentence.encode(),cli)
    print(cli,' -> ',sentence) 
    _thread.exit()
    serverSocket.close()

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((host, serverPort))
print('The server is ready to receive')
while True:
    message, cli =  serverSocket.recvfrom(2048)
    _thread.start_new_thread(conexao,(message,cli))
