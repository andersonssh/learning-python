import time
from types import FunctionType

def calcula_tempo(funcao: FunctionType) -> FunctionType:
    def wrapper():
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()

        print(f'[{funcao.__name__}] Tempo total de execucao: {tempo_final-tempo_inicial} ')

    return wrapper


@calcula_tempo
def funcao_principal():
    for n in range(1000000):
        a = 'asdasdasdasd'.replace('a', 'ad')

funcao_principal()