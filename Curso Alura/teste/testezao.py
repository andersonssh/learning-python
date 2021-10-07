#from testezin import *
import testezin
def seila():
    return teste(1)

def teste(a):
    print('Executando teste')
    return str(a) + ' esse é o valor da var'

print(seila())
print(__name__)

class Nome:
    def __init__(self):
        a = 0
    def oi(self, a):
        self.kk = 333333
        print(a)


a = Nome()
a.oi('a')
print(a.kk)