import datetime
class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def mostrar(self):
        print('Data de abertura: ', self.data_abertura)
        if len(self.transacoes):
            print('----Transacoes----')
        for i in self.transacoes:
            print('{}'.format('-=-' * 10))
            print(i)

class Conta:
    def __init__(self, conta, titular, limite = 1000):
        self.conta = conta
        self. titular = titular
        self.saldo = 0
        self.limite = limite
        self.historico = Historico()

    def saca(self, valor):
        if valor > self.saldo or valor < 0:
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append('\033[31mSaque no valor de : \033[34m{}\033[m'.format(valor))
            return True

    def deposita(self,valor):
        self.saldo += valor
        self.historico.transacoes.append('\033[32mDeposito no valor de: \033[34m{}\033[m' .format(valor))
        return True

    def transfere(self, conta, valor):
        if self.saca(valor):
            conta.__saldo += valor
            conta.historico.transacoes.append('\033[32mTransferencia de \033[mR$ \033[34m{:5.2f}\033[32m recebida de \033[m{}' .format(valor, self.titular.nome))
            self.historico.transacoes.append('\033[31mTranferencia de \033[mR$ \033[34m{:5.2f} \033[31mpara \033[m{}'.format(valor,conta.titular.nome))
            return True
        else:
            return False

    def extrato(self):
        print('\033[7mEXTRATO COMPLETO DA CONTA {}\033[m'.format(self.conta))
        self.titular.mostrar()
        print('Saldo atual da conta: R$ {:7.2f}' .format(self.saldo))
        self.historico.mostrar()


class Cliente:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar(self):
        print('Dados do cliente: |Nome: {} | Idade: {}'.format(self.nome, self.idade))

