def decorador(parametro_1, parametro_2):
    def envelope(funcao):
        def executa_funcao():
            print('parametro1: ', parametro_1)
            print('parametro2: ', parametro_2)
            # funcao() # tambem da certo
            return funcao()
        return executa_funcao
    return envelope

@decorador('parametro 1 aquiiiiii', 'parametro 2 aqui')
def funcao_aleatoria():
    print('dentro da funcao aleatoria')

funcao_aleatoria()

