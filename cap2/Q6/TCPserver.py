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


def agendarMonitoria():
    msg = '\n\nPara agendar uma moitoria, basta enviar um e-mail para cainafigueiredo@poli.ufrj.br\n'
    return msg

def atividadesPendentes():
    msg = '\n\nFique atento para as datas das próximas atividades. Confira o que vem por aí\n\nP1:26 de maio de 2022\nLista 3: 29 de maio de 2022\n'
    return msg

def emailProfessor():
    msg = '\n\nQuer falar com o Professor?\nO e-mail dele é sacod@dcc.ufrj.br\n'
    return msg

def goodBye():
    msg = '\n\nObrigado por utilizar os nossos serviços!\n\nAté logo!\n'
    return msg

def conexao(con, cli):
        req = con.recv(1024).decode()
        boasVindas = 'Olá! Bemvindo! Qual é o seu nome? '
        con.send(boasVindas.encode())
        user = con.recv(1024).decode()
        serviceMsg = f'\n\nCerto {user}! Como posso ajuda-lo?\n\n\n Digite o número que corresponde à opção desejada:\n\n\n1 - Agendar um horário de monitoria\n2 - Listar as próximas atividades da disciplina\n3 - Email do professor\n\n'
        con.send(serviceMsg.encode())
        req = con.recv(1024).decode()
        if req == '1':
            con.send(agendarMonitoria().encode())
        elif req == '2':
            con.send(atividadesPendentes().encode()) 
        elif req == '3':
            con.send(emailProfessor().encode())
        con.send(goodBye().encode())
        print('Close')
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
