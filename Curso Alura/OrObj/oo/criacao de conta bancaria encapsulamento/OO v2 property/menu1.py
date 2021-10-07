import contaBancaria

c = contaBancaria.Cont()
c1 = contaBancaria.Cont()

c.saca(90000)
c._Cont__seila = 30000000000
print(c._Cont__seila)
c.mostrar()
print(c.saldo)