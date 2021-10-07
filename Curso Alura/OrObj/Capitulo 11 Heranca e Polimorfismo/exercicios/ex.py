#class Conta(object): #a mesma coisa que a linha abaixo
class Conta:
    def __init__(self,titular,saldo):
        self._titular = titular
        self._saldo = saldo

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f'Dados da conta\nTitular:{self._titular}\nSaldo:{self._saldo:5.2f}'

class ContaCorrente(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2

    def deposita(self, valor):
        self._saldo += valor - 0.1

class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3


class Banco:
    contas = []
    def adiciona(self, conta):
        self.contas.append(conta)

    def get_total_contas(self):
        return len(self.contas)

class Cliente:
    pass




if __name__ == '__main__':
    c = Conta('Joze Zonza', 1000)
    cc = ContaCorrente('Jozezao Kria Corrente', 1000)
    cp = ContaPoupanca('Silvera Poup Zorel', 1000)
    cliente = Cliente()
    c.atualiza(0.01)
    a = c
    print('Olha o valor de a: ', a)
    print(c)#a funcao print chama o __str__ da classe
    cc.atualiza(0.01)
    cp.atualiza(0.01)
    a.deposita(5000)
    banco = Banco()
    banco.adiciona(c)
    banco.adiciona(cc)
    banco.adiciona(cp)
    banco.adiciona(cliente)
    banco.contas[0].deposita(2000)
    for i in banco.contas:
        if hasattr(i, 'atualiza'):
            i.atualiza(10)
        else:
            print(i, ' Nao possui atualizador de conta')
    print(c)
    print(cc)
    print(cp)