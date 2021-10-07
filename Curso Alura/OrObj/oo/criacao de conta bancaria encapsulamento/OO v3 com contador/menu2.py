from conta import *

c1 = Conta()
c2 = Conta()
print(c1.total_contas)
#tudo o que é alterado diretamente na classe fica visivel para todas as instancias
c3 = Conta()
print(c3.total_contas)
print(c2.total_contas)
print(c1.total_contas)