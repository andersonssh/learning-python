import os
import sys
path_para_arquivo_atual = os.path.abspath(__file__)
# caminho/completo/ate/o/arquivo.py
print(path_para_arquivo_atual)

diretorio_atual = os.path.dirname(path_para_arquivo_atual)
# caminho/completo/ate/a/pasta/pai/do/  -> arquivo.py
print(diretorio_atual)

pai_do_diretorio_atual = os.path.dirname(diretorio_atual)

# sys.path tras todos as pastas e os arquivos conhecidas pelo arquivo de onde é chamado
# ao adicionar o diretorio atual ou o pai do diretorio atual, é possivel
# acessar os arquivos dentro desses diretorios como se o arquivo
# atual (quem chama) fosse irmao do arquivo que é chamado
# tendo em vista que, quando um arquivo python é executado, ele só enxerga
# irmaos e filhos dos irmaos mas não enxerga o diretorio pai e muito menos
# os diretorios irmaos do pai
if diretorio_atual not in sys.path:
    sys.path.append(diretorio_atual)
    pass
if pai_do_diretorio_atual not in sys.path:
    sys.path.append(pai_do_diretorio_atual)
    pass

from pasta1 import arq_principal

print(arq_principal.variavel)


# este arquivo pode ser um __init__.py e assim todos os arquivos do modulo
# podem acessar outras pastas "distantes"