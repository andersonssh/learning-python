class Teste:
    def __init__(self, t):
        self.t = t

    @staticmethod
    def teste():
        # este metodo é independente da classe
        print('ola')
        # logo a linha abaixo seria impossivel
        # print(self.t)

Teste('j').teste()
