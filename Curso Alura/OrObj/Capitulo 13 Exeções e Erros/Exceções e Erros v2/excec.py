class Conta:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo


    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    def saca(self, valor):
        self._saldo -= valor

    def deposita(self, valor):
        self._saldo += valor



if __name__ == '__main__':
    try:
        a = 1/10
    except(ZeroDivisionError, NameError) as e:
        print(e)
    else:
        print('Sucesso!!!!! A foi definido')

    print
    print('aaa')