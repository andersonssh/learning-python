class Conta:
    __total_contas = 0
    def __init__(self):
        self.saldo = 0
        Conta.__total_contas += 1

    @property
    def total_contas(self):
        return Conta.__total_contas #quando é um atributo de classe
        #deve ser referenciado com Classe.atributo


