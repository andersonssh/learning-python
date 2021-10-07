import socket
ip = socket.gethostbyname('www.tudosaladeaula.com')
print('Ip do google:', ip)
print(socket.getservbyname('http'))
print(socket.getservbyname('domain'))
print(socket.getservbyname('ftp'))