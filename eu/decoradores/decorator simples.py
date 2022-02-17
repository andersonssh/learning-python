def decorator(funcao):
    def wrapper():
        print('Antes de executar a funcao')
        funcao()
        print('Depois de executar a funcao')

    return wrapper

def outra_func():
    print('funcao principal!')

# a linha abaixo é equivalente as ultimas linhas
# decorator(outra_func)()

funcao_decorada = decorator(outra_func)
funcao_decorada()