class Conta:
    #Protege contra a insercao de atributos fora da classe
    __slots__ = ['seila']
    #o uso de slots melhora em 40% o uso de memoria ram
    #pois o dict usa muita memoria na criacao de atributos
    #em muitas instancias
    #e deixar atributos fixos ajuda no processo

    _total_contas = 0
    def __init__(self):

        self.seila = 0
        print(type(self), self)
        type(self)._total_contas += 1

    @classmethod
    def get_total_contas(cls):
        return cls._total_contas

    @staticmethod
    def get_tot():
        return Conta._total_contas


