import conta

c = conta.Conta()
#c.kkk = 1

#com o slots ativado o interpretador do python deleta o atributo __dict__
#print(c.__dict__)
print(c.get_total_contas())
print(c.get_tot())
print(conta.Conta.get_tot())