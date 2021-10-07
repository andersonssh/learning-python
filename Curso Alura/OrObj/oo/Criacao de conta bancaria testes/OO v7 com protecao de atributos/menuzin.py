import conta

cliente = conta.Cliente('Josezao', 18)
contaa = conta.Conta(1983, cliente)
cliente1 = conta.Cliente('Josezinnn', 20)
conta1 = conta.Conta(1812, cliente1)

contaa.deposita(1000)
contaa.saca(999)
contaa.deposita(123)
contaa.transfere(conta1, 100)

contaa.__saldo = 300000000 #de nada serve pois o atributo é privado
contaa._Conta__saldo = 30000 #alterando o atributo privado diretamente
contaa.extrato()
print('~' * 30)
print(dir(contaa))
conta1.extrato()

#Altera o atributo privado!!!!!!!!!!!!!!!!!!!
#contaa._Conta__saldo = 30000