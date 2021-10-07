from contaa import ContaBancaria

c = ContaBancaria('seila silva souza', 1231)
print(c.titular, c.saldo)

c1 = c
c1.saca(99)
c1.deposita(999)
c1.deposita(1)
c1.saca(10)

print(c1.titular, c1.saldo)
x = 0
print('\n\n IDS: ',id(c1), id(x))
print(id(c) == id(c1), c, c1)