import conta

cliente = conta.Cliente('Josezao', 18)
contaa = conta.Conta(1983, cliente)
cliente1 = conta.Cliente('Josezinnn', 20)
conta1 = conta.Conta(1812, cliente1)

contaa.deposita(1000)
contaa.saca(999)
contaa.deposita(123)
contaa.transfere(conta1, 100)
contaa.extrato()
print('~' * 30)
conta1.extrato()
print(vars(contaa))