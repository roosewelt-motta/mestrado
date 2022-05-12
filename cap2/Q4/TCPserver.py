from socket import *
import _thread

host = ''
serverPort = 12000

def conexao(con, cli):
    print('Client: ', cli)
    while True:
        sentence = con.recv(2048).decode()
        if not sentence:
            break
        capSen = sentence.upper()
        con.send(capSen.encode())
        print(cli,' -> ',capSen) 
    print('Close ', cli)
    con.close()
    _thread.exit()

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((host, serverPort))
serverSocket.listen(1)
print('TCPi Server is ready')
while True:
    con,cli =  serverSocket.accept()
    _thread.start_new_thread(conexao,(con,cli))
serverSocket.close()
