class Cont:
    def __init__(self,saldo = 0.0):
        self.__saldo = saldo
        self.__seila = 0

    @property
    def saldo(self):
        print('Oolooooooooookoooooo')
        return self.__saldo


    def mostrar(self):
        print(self.__saldo, self.__seila)

    def saca(self, valor):
        self.__saldo = valor




