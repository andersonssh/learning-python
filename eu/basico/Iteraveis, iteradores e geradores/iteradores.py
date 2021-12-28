# criando um iteravel
lista = [1,2,3,4,5]
# é um iteravel?
print(hasattr(lista, '__iter__'))
# é um iterador?
print(hasattr(lista, '__next__'))

# tranformando a variavel lista em um iterador
lista2 = iter(lista)
# é um iteravel?
print(hasattr(lista2, '__iter__'))
# é um iterador?
print(hasattr(lista2, '__next__'))

print('exibindo lista:', lista, 'exibindo lista2:', lista2)


# avancando em um iterador
# erro pois lista nao é um iterador!
# print(next(lista))

import sys
print('tamanho da var lista:', sys.getsizeof(lista))
print('tamanho da var lista2:', sys.getsizeof(lista2))
# avanca no iterador
print('valor: ', next(lista2))
print(sys.getsizeof(lista2))
print('valor: ', next(lista2))
# tem o  mesmo efeito que as linhas a cima
for i in lista2:
    print('valor: ', i)
print('--------------------- fim exibicao lista2 ------------------')

# quanto maior a lista maior o espaco ocupado em memoria
# apesar do numero de itens, um iterador permanece com a mesma quantidade de espaco em memoria

print('--------------------------')

# range retorna um iterador
print(sys.getsizeof(range(10)))
print(sys.getsizeof(range(100)))
print(sys.getsizeof(range(1000)))
print(sys.getsizeof(range(10000)))
