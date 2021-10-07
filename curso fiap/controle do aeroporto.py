dados = []
def transformar_em_float(ind):
    for i in range(len(dados[ind])):
        dados[ind][i] = float(dados[ind][i])


with open('economic-indicators.csv', 'r') as ct:
    for i in ct:
        dados.append(i.strip('\n').split(','))
for i in range(1,len(dados)):#len(dados[1:] retorna a quantidade total menos 1 assim sendo só vai iterar até a penultima linha
    transformar_em_float(i)

# for j in range(len(dados[0])):
#     print(f'{dados[0][j]}: ', end=' ')
#     for i in range(1,len(dados)):
#         print(dados[i][j], end= ' ')
#     print()
total = 0
for i in range(1,len(dados)):
    total += dados[i][3]
print('Total de voos: ', total)
maiorValor = 0
mes = 0
for i in range(1,len(dados)):
    if dados[i][2] > maiorValor:
        maiorValor = dados[i][2]
        mes = dados[i][1]

print('Mês mais lotado: ', mes)
opMes = float(input('DIGITE O MES DA CONSULTA: '))
for i in range(1, len(dados)):
    if dados[i][1] == opMes:
        print(f'No ano de {dados[i][0]} no mes {opMes} estiveram presentes no aeroporto {dados[i][2]} pessoas')

opAno = float(input('Digite o ano da consulta: '))

for i in range(1, len(dados)):
    if dados[i][0] == opAno:
        print(f'No ano de {opAno} foram registradas {dados[i][5]} pessoas no hotel')

