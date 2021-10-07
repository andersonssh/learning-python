from conta import Conta

c = Conta()
c.titular = 'opa mudei aki de fora'
print(c.titular,c.numero, sep='\n-=-\n')
c.ola()

c1 = Conta()
c1.nova = 'atributo adicionado dinamicamente (durante a execucao)'
print(c1.titular,c1.numero, c1.nova, sep='____')
print()
c1.ola()