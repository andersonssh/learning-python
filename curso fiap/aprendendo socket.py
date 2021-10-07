from socket import *

def envia_comando(sock, comando):
    comando += '\r\n'
    sock.send(comando.encode('UTF-8'))


def registra(sock, nick):
    envia_comando(sock, 'NICK {}'.format(nick))
    envia_comando(sock, 'USER {0} {0} {0} : {0}'.format(nick))
    print('enviando comando USER {0} {0} {0} : {0}'.format(nick))


soquete = socket(AF_INET, SOCK_STREAM)
soquete.connect(('irc.rizon.net', 6667))
nick = 'Seilaasdasd'
registra(soquete, 'BotDaEmpresa')
dados = soquete.recv(2048).decode('UTF-8')
print(dados)