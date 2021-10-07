def criaConta(numero, titular, saldo, limite):
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta

def deposita(conta, valor):
    conta['saldo'] += valor

def saca(conta, valor):
    conta['saldo'] -= valor

def extrato(conta):
    print('Numero: {}\nTitular: {}\nSaldo: {}'.format(conta['numero'], conta['titular'], conta['saldo']))

c1 = criaConta(11231,'Joao fereira souza', 123.99, 500)
c1['saldo'] = 3000000
saca(c1, 100000)
extrato(c1)