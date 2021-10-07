s = 'curso em video aulas          de       python'
ss = input('Nome da pessoa: ').strip #nesta linha ja serao eliminados espacos antes e espacos depois

print(len(s) - s.count(' '))
print(len(s.split()[0]))

print('caju e caja'.rfind('a'))