from eu.modulos.pasta1.arq_principal import variavel

print(variavel)
# todos os arquivos podem acessar os arquivos filhos da pasta pai
# diretamente atraves de um import nome_do_arquivo
# o sys.path (objeto q o interpretador usa para visualizar os arquivos)
# inclui a pasta raiz do projeto (onde o interpretador está rodando)
# checar mais anotacoes na pasta "/modularizacao"