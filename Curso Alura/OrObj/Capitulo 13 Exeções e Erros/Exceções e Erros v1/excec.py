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
    def metodo1():
        print('início do metodo1')
        metodo2()
        print('fim do metodo1')


    def metodo2():
        print('início do metodo2')
        cc = Conta('José', 0)

        for i in range(1, 15):
            cc.deposita(i + 1000)
            print(cc.saldo)
            if i == 5:
                cc = None
        print('fim do metodo2')

    print('início do main')
    try:
        metodo1()
    except:
        print('Erro')
    print('fim do main')