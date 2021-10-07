s = 'curso em video'
print(s.count('o',1,9)) #conta quantos 'o' encontra na fatia, (fatiamento opcional)
print(s.find('o'))#encontra o indice da primeira ocorrencia de 'o' na fatia ou string completa
print(s.find('em '))#tb encontra sequencia de caracteres e retorna o indice do primeiro..
#se nao existir retorna -1
print('curso' in s)
print(s.replace('curso','curso mod do curso'))#sempre que houver uma ocorrencia do primeiro parametro
#ele substitui pelo segundo parametro e retorna uma string
#os parametros podem ser string ou caracter
print(s.replace('e','M'))
print(s.upper())
print(s.capitalize())#transforma todos os caracteres em minusculos e só upp o primeiro
print(s.title())#coloca toda palavra com a primeira letra em maiuscula
print('   ' + s + '   ')#strip por padrao remove espacos desnecessarios no inicio e no fim das strings
print(('   ' + s + '   ').strip())#rstrip remove somente os ultimos espacos e lstrip da esquerda
#strip tambem pode ser usado para remover caracteres de strings...
print(s.split())#separa string de acordo com o parametro dado que por padrao é o espaco
print(s.split('v'))
print('-'.join(s))#junta listas usando separador o delimitador escolhido previamente..
#usando diretamentem uma string temos este resultado na tela
print('-'.join(['curso', 'em', 'video']))
print("""Poema é um gênero textual dividido em estrofes e versos. 
Cada estrofe é constituída por versos. Introduzidos pelo sentido das frases - 
e mais raramente em conversa - em que a poesia, forma de expressão estética através da língua,
geralmente se manifesta. Wikipédia""")


lista = ['seila', 'opsss']
print(lista[1][2])#mostrando indice 1 e a letra do indice 2
print('caju e caja'.find('a'))
print('caju e caja'.rfind('a'))#o "r"find faaz a busca inversa... da direita para a esquerda