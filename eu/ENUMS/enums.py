from enum import Enum


class Features(Enum):
    LETRA_A = {'a': 'A'}
    LETRA_B = {'b': 'B'}
    LETRA_A_B = {'a': 'A', 'b': 'B'}

print(Features['LETRA_A'].value['a'])
print({i.name: i.value for i in Features})
print('LETRA_A' in Features.__members__)