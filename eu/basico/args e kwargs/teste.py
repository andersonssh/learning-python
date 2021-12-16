# args -> argumentos
# kwargs -> argumentos de palavras-chave

def teste(*args):
    print(*args)
    print(args)
    print(type(args))
    print(sum(args))

teste()
teste(1,2,3,4,5)

print('-------------FIM ARGS---------------')

def testeK(**kwargs):
    print(kwargs.items())
    print(kwargs)
    print(type(kwargs))

testeK()

print('-----------------------------')

testeK(seila=0, teste='dicio ON')
