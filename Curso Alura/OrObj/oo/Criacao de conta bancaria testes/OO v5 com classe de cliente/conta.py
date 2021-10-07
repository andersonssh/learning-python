class ContaBancaria:
    def __init__(self,titular, saldo:float):
        print('Criando Nova Conta')
        self.titular = titular
        self.saldo = saldo

    def saca(self, saldo):
            self.saldo -= saldo
            print('Novo valor de saldo apos saque de {}: {} '.format(saldo, self.saldo))

    def deposita(self, valor):
        self.saldo += valor
        print('Novo valor de saldo apos deposito de {}: {} ' .format(valor, self.saldo))

    def transfere(self,destino, valor):
        if self.saldo < valor or valor < 0:
            print('Erro ao transferir... valor insuficiente <P')
            return False
        else:
            self.saldo -= valor
            destino.__saldo += valor
            print('Valor transferido com sucesso! <P')
            return True

    def extrato(self):
        print('Dados do titular: ->cpf e idade: ',self.titular.cpf, self.titular.idade,'\nDados da conta: -> saldo: {:9.2f}'.format(self.saldo))

class Cliente:
    def __init__(self, cpf, idade):
        self.cpf = cpf
        self.idade = idade