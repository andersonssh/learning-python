import abc
class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def seila(self):
        print('Olaa testando super')

class Cadastro:
    def __init__(self, usuario):
        self.usuario = usuario

    def teste(self):
        print('Teste de super hahah')

#mixin sinaliza que e uma classe que adiciona funcoes
class BixaoMixIn:
    def bixao(self):
        #aqui foi criado self.atributo que nao esta presente nesta classe
        #o interpretador ira procurar este atributo na classe filha
        #tambem encontrara caso a classe filha tenha herdado de outra classe...
        #o self é bem versatil pois ele age como se estivesse na classe solicitante
        #tendo o mesmo efeito que chamar um metodo de fora da classe
        #pois lá ele mostra metodos e atributos que sao de classes maes por exemplo...
        print('Tu e o bixao mermo hein doido')
        if hasattr(self, 'senha'):  # o self quando executado vera em que classe ele esta e executa em seguida!
            # neste caso ele verifica se a classe solicitante possui o atributo ou metodo senha
            print('Mostrando senha Por meio de funcao em classe mae:', self.senha)

        else:
            print('Nao possui senha')  # caso nao tenha exibe esta mensagem
        if hasattr(self, 'nome'):
            print('Nome do individuo em self por classe externa: ', self.nome)
        else:
            print('Nao possui nome')


class Altenticavel(abc.ABC):
    @abc.abstractmethod
    def autentica(self, senha):
        #print('Senha correta, ', senha)
        pass


class Gerente(Funcionario, Cadastro, BixaoMixIn):
    def __init__(self, nome, senha, usuario):

        # super().__init__(nome)
        # super().__init__(usuario)
        #quando os metodos forem com o mesmo nome entao
        #devem ser referenciados pelas classes e passar self
        #como parametro inicial pois eles fazem parte da classe
        #atual(Gerente)
        Funcionario.__init__(self, nome)
        Cadastro.__init__(self, usuario)
        #o super detecta a que classe pertence o metodo requisitado... exceto metodos com o mesmo nome
        #daii o metodo acima é o mais indicado!!!!!!!!!!!!!!!!!!!!!!!!!
        super().seila()
        super().teste()
        self.senha = senha


g = Gerente('José', 123, 'seila12345')

print(g.nome,g.senha, g.usuario)

g.bixao()
