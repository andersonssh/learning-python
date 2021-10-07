class ContaBancaria:
    def __init__(self,titular, saldo):
        print('Criando Nova Conta')
        self.titular = titular
        self.saldo = saldo

    def saca(self, saldo):
            self.saldo -= saldo
            print('Novo valor de saldo apos saque de {}: {} '.format(saldo, self.saldo))

    def deposita(self, valor):
        self.saldo += valor
        print('Novo valor de saldo apos deposito de {}: {} ' .format(valor, self.saldo))
