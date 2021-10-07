class Conta:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo

    def saca(self, valor):
        if valor > self._saldo:
            raise SaldoInsuficienteError('Saldo insuficiente!')
        elif valor < 0:
            raise ValueError('Saque com valor negativo não é permitido!')
        else:
            self._saldo -= valor

    def deposita(self, valor):
        if valor < 0:
            raise ValueError('Você tentou depositar um valor negativo!')
        else:
            self._saldo += valor

class SaldoInsuficienteError(RuntimeError):
    ...


if __name__ == '__main__':
    cc = Conta('seila', 100)

    try:
        cc.saca(-1000)
    except (ValueError, SaldoInsuficienteError) as E: #esta linha permite nomearr o apelido E com o valor do erro em questao
        print(E)
    else:
        print('Saque realizado!')

