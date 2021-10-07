import os
from ftplib import FTP as ftp

nonpassive = False
Arquivo = 'README'
dir = 'debian'
site = 'ftp.debian.org'
usuario = []
print('Conectando...')
conexao = ftp(site)
conexao.login(*usuario)
conexao.cwd(dir)
print(conexao.retrlines('LIST'))
