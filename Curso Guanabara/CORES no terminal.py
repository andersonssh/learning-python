apresentacao = 'Olá  eu sou um programador'
bv = 'SEJA bem vindo'
agradecimento = 'Obrigado por testar meu programa'
xau = 'Até mais ver, bon voyaaj arriverdec'

'''print('\033[0:33:44m',apresentacao)
print('\033[1:33:44m',apresentacao)
print('\033[4:33:44m',apresentacao)
print('\033[7:33:44m',apresentacao)'''

bv = '\033[0;30;41m' + bv
print(bv)
#\033[m desfaz todas as configuracoes e volta ao padrao
print('\033[1;35;43m Olá\033[m')
print('\033[30;42m OLaaaaaaaaaa')