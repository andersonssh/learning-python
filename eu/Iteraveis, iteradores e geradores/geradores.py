import sys
import time

def gera():
    r = []
    for i in range(100):
        r.append(i)
        print('executando sleep n:', i)
        time.sleep(0.1)
    return r

# aqui a funcao demora bastante para executar pois ela carrega
# todos os dados do loop for para retorna-los todos de uma vez
# g = gera()
#
# print(g)
# for x in g:
#     print(x)


# transformando a funcao gera em funcao geradora

def gera2():
    for i in range(100):
        yield i
        print('executando sleep')
        time.sleep(0.1)

# aqui, cada loop do for só é executado quando necessário

# g2 = gera2()

# for z in g2:
#     print(z)

# ao invez de usar um for a funcao next também é valida!
# print(next(g2))
# porem, se executado quando o ultimo item já tiver sido usado, ele retorna o erro StopIteration

# print(hasattr(g2, '__next__'))
# # >>> True
# print(hasattr(g2, '__iter__'))

def gera3():
    var = 'V1'
    # as linhas seguintes só sao executadas quando o valor da variavel é acessado
    yield var
    yield 'v3'
    yield 'v12'

g3 = gera3()
print(next(g3))
print(next(g3))
print(next(g3))

