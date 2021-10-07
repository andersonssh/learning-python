import random
nomes = ['lucas', 'mateus', 'luiza', 'jorge']
#solucao do prof
random.shuffle(nomes)

for i in nomes:
    print(i)
#fim solucao do prof
print('\nFIM da solucao do prof.\n')

#Mostrando ordem dos alunos a apresentarem o trabalho
for i in range(4, 0, -1):
    x = random.randint(1,i) -1
    print(nomes.pop(x))

random.shuffle(nomes) #embaralha uma lista

#solucao do prof
for i in nomes:
    print(i)

