import os
from time import sleep
cores = {'vermelho': '\033[31m','inverter': '\033[7m', 'verde': '\033[32m', 'limpar': '\033[m', 'azul':'\033[1;35m'}
def menu():
    """
    Menu principal
    :return: str digitada pelo usuario sinalizando a opção
    """
    #os.system('clear')
    print(f'{cores["azul"]}\t\tJOGO DO FUTURO{cores["limpar"]}')
    global opcoes
    opcoes = ['INICIAR']
    print(cores['verde'], end='')
    for i in range(len(opcoes)):
        print(f'[{i+1}] {opcoes[i]}')
    print(cores['limpar'], end='')
    print(f'\n{cores["vermelho"]}[0] SAIR{cores["limpar"]}')
    return input('\nOpção: ')

def error():
    print('Erro!!! Tente novamente')
    sleep(1)


def iniciar():


def verifica_valor(maximo, opcao):
    """
    Verifica se o valor está entre os numero permitidos
    :param maximo: valor maximo do menu
    :param opcao: opcao marcada
    :return: Boolean
    """
    if type(opcao) != 'int':
        try:
            opcao = int(opcao)
        except:
            error()
            return False
    if opcao < 0 or opcao > maximo:
        return False
    else:
        return True

if __name__ == '__main__':
    opcao = menu()
    while not verifica_valor(len(opcoes), opcao):
        opcao = menu()

    if opcao == 1:
        iniciar()
    elif opcao == 0:
        exit()


