from conta import ContaBancaria

c = ContaBancaria('Josef', 100)
c1 = ContaBancaria('Bryan', 300)

if c.transfere(c1, int(input('Quanto deseja transferir: '))):
    print('Estado Final: Transferido!')
else:
    print('Estado Final: Nao transferido')
print(c.titular,c.saldo)
print(c1.titular, c1.saldo)