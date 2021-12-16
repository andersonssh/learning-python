def meu_decorador(funcao):
    def func_que_roda_func(funcao):
        print('--------INICIANDO FUNCAO EMBRULHADA------------')
        funcao()
        print('--------TERMINANDO FUNCAO EMBRULHADA------------')
    return func_que_roda_func(funcao)

def minha_funcao():
    print('ola')

# o decorador executa a funcao!
@meu_decorador
def minha_funcao_v2():
    print('ola2')

