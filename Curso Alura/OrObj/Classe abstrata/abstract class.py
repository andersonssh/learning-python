import abc
class Funcionario(abc.ABC):
    numero_de_pessoas = 0
    def __init__(self, nome, cpf, salario, nivel_de_poder=1):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        Funcionario.numero_de_pessoas += 1
        self._nivel = nivel_de_poder

    @abc.abstractmethod
    def get_bonificacao(self):
        pass



class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, nivel_de_poder, senha):
        super().__init__(nome, cpf, salario,nivel_de_poder)
        self.senha = senha

    def autentica(self, senha):
        if self.senha == senha:
            print('Acesso Permitido')
            return True
        else:
            print('Acesso negado')
            return False

    def get_bonificacao(self):
        return 'seilaaaaaa'

    def mostrar(self):
        print('Senha: {} '.format('*' * len(self.senha)), end=' ')
        super().mostrar()



class ControleDeBonificacoes:
    def __init__(self, total_bonificacoes=0):
        self._total_bonificacoes = total_bonificacoes
    def registra(self, funcionario):
        self._total_bonificacoes += funcionario.get_bonificacao()
    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes

class Cliente:
    def __init__(self, nome, cpf, senha):
        self._nome = nome
        self._cpf = cpf
        self._senha = senha

if __name__ == '__main__':
    gerente = Gerente('aaa','aa', 999, 1,123123)
    clientee = Cliente('aa',123,123)
print(isinstance(gerente, Funcionario))
print(isinstance(clientee, Funcionario))