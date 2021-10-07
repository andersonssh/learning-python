class Computador:
    def __init__(self,marca, memoria, placa):
        self.marca = marca
        self.memoria = memoria
        self.placa = placa
        self.valor = 1

    def incrementa(self, v, i):
        valor = v
        self.incremento = i
        resultado = v + i
        return resultado

    def ligar(self):
        print('Computador Ligando')

    def desligar(self):
        print('Computador Desligando')
        return 0

    def exibirInformacoesDoPc(self):
        print(self.marca, self.memoria, self.placa)


c1 = Computador('','','').incremento(10,1)
print(c1.incremento)

print(c1)
c2 = Computador('Dell', '11 gb', 'Seila')
print(c2.valor)

