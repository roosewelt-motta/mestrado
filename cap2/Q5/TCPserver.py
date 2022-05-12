from socket import *
import _thread

host = ''
serverPort = 12000

def doLogin(user, password):
    auth = False
    if user == 'sadoc':
        if password == 'daniel':
            auth = True
    return auth        

def conexao(con, cli):
    print('Client: ', cli)
    
    authMsg = 'Bad credentials'
    loginMsg = 'Login Acess: '
    passMsg = 'Password: '
    retries = 3
   
    while retries > 0:
        msg = con.recv(2048).decode()
        con.send(loginMsg.encode())
        loginTxt = con.recv(16).decode().lower()
        con.send(passMsg.encode())
        passTxt = con.recv(16).decode()

        if doLogin(loginTxt, passTxt):
            authMsg='Login OK'
            con.send(authMsg.encode())
            break
        con.send(authMsg.encode())
        print(loginTxt,' : ',authMsg) 
        retries -= 1
    print('Close ', cli)
    con.close()
    _thread.exit()

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((host, serverPort))
serverSocket.listen(1)
while True:
    print('TCP Server is ready')
    con,cli =  serverSocket.accept()
    _thread.start_new_thread(conexao,(con,cli))
    
serverSocket.close()
