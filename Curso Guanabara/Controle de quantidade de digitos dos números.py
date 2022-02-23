k = 'seila velio'
for i in range(150): #{:x} diz quantos digitos o num vai ocupar independente do tamanho
    #print('{:3}'.format(i))
    print(f'{i:3}, testando string: {k:1}')
    
print("{:04d}".format(1)) # 0001
print("{:04d}".format(323)) # 0323
print("{:04d}".format(55555)) # 55555

print("%04d" % (1)) # 0001

print(f"{1:04d}") # 0001
