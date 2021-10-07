class Conta:
    def __init__(self, numero, titular, saldo, limite = 1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

    @property
    def numero(self):
        print('Usando o propertiiiiii')
        return self._numero

    def deposita(self, valor):
        self._saldo += valor


if __name__ == '__main__':
    conta = Conta('123-4', 'Joaozao Souzao', 1000.0)
    print(conta._titular)
    conta.deposita(500)
    print(conta.numero)
