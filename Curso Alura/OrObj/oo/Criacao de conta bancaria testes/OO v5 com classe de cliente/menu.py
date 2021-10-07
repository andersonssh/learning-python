from conta import ContaBancaria, Cliente

cliente1 = Cliente(231231312, 18)
cb = ContaBancaria(cliente1, 9.8)

cb.extrato()
