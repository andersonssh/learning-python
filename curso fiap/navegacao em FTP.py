from ftplib import *
ftp_ativo=False
ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())
usuario=input("Digite o usuario: ")
senha=input("Digite a senha: ")
ftp.login(usuario, senha)
while True:
    x = input(ftp.pwd() + '> ')
    if x.split(' ')[0] == 'cd':
        ftp.cwd(x.split(' ')[1])
    elif x == 'dir':
        print(ftp.retrlines('LIST'))
    else:
        print('Comando inválido')

    print(ftp.retrlines('LIST'))
ftp.quit()