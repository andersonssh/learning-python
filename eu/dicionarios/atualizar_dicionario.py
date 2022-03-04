a = [{'teste': 'ok'}, {'teste2': 'ok2'}]
b = a[0]
print('var a:', a)
print('var b:', b)

print('--------------------------------')

b.update({'teste': 'ALTERADO!', 'tst': 'item adicionado'})


print('var b atualizada:', b, end='\n\n')

# o dicionario da lista de A tambem foi alterado pela alteracao direta na var "b"
print('var a atualizada:', a)

