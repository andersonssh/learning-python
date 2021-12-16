# manipulando propriedades das classes
# METODOS DE CLASSE

class Teste:
    teste1 = 1

    def __init__(self, t):
        self.teste2 = t

    @classmethod
    def teste(cls):
        # este metodo altera atributos nativos da classe
        # para todas as instancias atuais e futuras!
        pass


a = Teste('jj')

print(a.teste2)
# exemplo sem alteracao direta da propriedade da classe
print(a.teste1)

# alterando propriedade de classe diretamente
Teste.teste1 = 3

b = Teste('kk')

print(b.teste2)

# as alteracoe feitas na linha 22 repercutiram em todas as instancias
print(b.teste1)
print(a.teste1)
print(a.teste2)

print('------------------------------------------------')

class Teste2:
    teste1 = 1

    def __init__(self, t):
        self.teste2 = t

    @classmethod
    def teste(cls):
        cls.teste1 = 55

    @classmethod
    def testeC1(cls):
        cls.teste1 = 80


a = Teste2('pp')

print(a.teste1)
print(a.teste2)
#linha altera o valor de todas as instancias!!!!!!
a.teste()

b = Teste2('gg')

print(b.teste1)
print(b.teste2)

# a linha 51
print(a.teste1)


print('------------------------------------------')

class Teste3(Teste2):
    t = 0

Teste3('jj').testeC1()

c = Teste3('jj')

# a casse pode herdar as alteracoes e fazer as proprias alteracoes em suas proprias instancias
print(c.teste1)

# as alteracoes feitas no atributo da classe herdeira nao foi realizado na classe pai
print(b.teste1)