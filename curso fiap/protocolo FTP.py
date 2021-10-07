from ftplib import *
ftp_ativo = False
ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())
ftp.login(input('Usuario:'), input('Senha:'))
print('Diretorio atual de trabalho:', ftp.pwd())
ftp.quit()