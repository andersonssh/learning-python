l = [0, 1, 2, 3]
s = 'Olá!'
n = 123

# verificando se as variaveis são iteráveis

# hasattr verifica se o atributo existe no objeto
# a presenca do atributo __iter__ diz que o objeto é iteravel
# logo, também pode ser usado em um laço for x in objIteravel
print(hasattr(l, '__iter__'))
for i in l:
    print(i)

print(hasattr(s, '__iter__'))
print(hasattr(n, '__iter__'))

import sys

# exibe tamanho em memoria

print(sys.getsizeof([1, 2, 3, 4, 5]))
print(sys.getsizeof(['1', '2', '3', '4', '5']))
print(sys.getsizeof([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(sys.getsizeof(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']))


print('----------------')

print(sys.getsizeof(list(range(10))))
print(sys.getsizeof(list(range(100))))
print(sys.getsizeof(list(range(1000))))
print(sys.getsizeof(list(range(10000))))
