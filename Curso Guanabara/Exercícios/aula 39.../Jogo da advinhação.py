from time import sleep
from random import randint
computador = randint(1,5)
humano = int(input('Digite um numero de 1 a 5: '))
print('PROCESSANDO...')
sleep(1)
print('-' * 20)
if humano == computador:
    print('Você acertou!')
else:
    print('Você errou" Você digitou {} e eu pensei no número {}' .format(humano, computador))