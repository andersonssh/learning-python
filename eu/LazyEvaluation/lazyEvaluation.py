from time import sleep

# nesta linha, python avalia imediatamente todos os itens da lista
# print([sleep(1), sleep(2), sleep(3)])

#### teste de memoria
# Python 2.7.16
# >>> range (5)
# [0, 1, 2, 3, 4]
# >>> import sys
# >>> sys.getsizeof (range (5))
# 112 (quantidade de espaco ocupado em memoria)
# >>> sys.getsizeof (range (500 ))
# 4072 (quantidade de espaco ocupado em memoria)

# Python 3.7.7
# >>> range (5)
# range (0, 5)
# >>> import sys
# >>> sys.getsizeof (range (5))
# 48 (quantidade de espaco ocupado em memoria)
# >>> sys.getsizeof (range (500))
# 48 (quantidade de espaco ocupado em memoria)

import sys
print(sys.getsizeof(range(5)))
print(sys.getsizeof(range(50000)))

# exibe mensagem de contexto de execucao e retorna o valor de v passado como parametro
def r(v, context):
    print('executando {}'.format(context))
    return v

l1 = [r(i, 'L1') for i in range(1000)]
l2 = (r(i, 'L2') for i in range(1000))
print(type(l1), sys.getsizeof(l1))
print(type(l2), sys.getsizeof(l2))

# def gera():
#     for i in range(1000):
#         yield r(i, 'L2')
# É O MESMO QUE
# (r(i, 'L2') for i in range(1000))