class Funcionario:
    numero_de_pessoas = 0
    def __init__(self, nome, cpf, salario, nivel_de_poder=1):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        Funcionario.numero_de_pessoas += 1
        self._nivel = nivel_de_poder

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nomee):
        self._nome = nomee

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, n_cpf):
        if '-' not in n_cpf:
            print('Cpf nao tem o -... Invalido!')
        else:
            self._cpf = n_cpf
    @property
    def nivel(self):
        return self._nivel
    @nivel.setter
    def nivel(self, nivel):
        print('Alterando Nivel!!!')
        self._nivel = nivel

    def get_bonificacao(self):
        return self._salario * 0.1


    def __str__(self):
        return 'Instancia de {} localizada em {}'.format(self.__class__.__name__, id(self))

    def mostrar(self):
        print('Nome: {} | CPF: {} | Salário: {:.2f} | nP: {}'.format(self._nome, self._cpf, self._salario, self.numero_de_pessoas))


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
    funcionario = Funcionario('João', '111111111-11', 2000.0)
    gerente = Gerente('aaa','aa', 999, 1,123123)
    clientee = Cliente('aa',123,123)
    if hasattr(funcionario, 'get_bonificacao'):
        print('GET_BONIFICACAO() EXISTE')

    else:
        print('GET_BONIFICACAO() NAO EXISTE')

print(isinstance(funcionario, Funcionario))
print(isinstance(gerente, Funcionario))
print(isinstance(clientee, Funcionario))