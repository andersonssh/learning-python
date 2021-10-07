from socket import *

servidor="127.0.0.1"
porta=43210

while True:
    sk = socket(AF_INET, SOCK_STREAM)
    sk.connect((servidor, porta))
    msg = bytes(input("Sua mensagem: "), 'utf-8')
    sk.send(msg)
    resposta= sk.recv(1024)
    print("Resposta do Servidor: ", str(resposta)[2:-1])
