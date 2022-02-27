from modularizacao import variavel

print(variavel)

# todos os arquivos python, independentemente da pasta onde está localizado
# enxerga os arquivos presentes no diretorio
# base onde o interpretador está rodando pois em
# sys.path, cada arquivo enxerga tambem o diretorio raiz do projeto!!!!!!!!!

import sys
print(sys.path)

# LOGO QUALQUER ARQUIVO DO PROJETO PODE SER ACESSADO ATRAVES DOS CAMINHOS
# imagine os arquivos
# / = pasta raiz do projeto
# /teste1/testefilho1/t1.py
# e
# /teste2/testefilho2/t2.py

# estes arquivos sao acessiveis um ao outro seguindo o modelo

# exemplo de arquivo t1.py acessando t2.py

# from teste1.testefilho import t1

