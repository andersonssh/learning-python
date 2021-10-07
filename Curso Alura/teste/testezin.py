a = [1,2,3,4,5,6]

def teste(v,k):
    return v+1

k = map(teste, a, a)
print(k)

for i in k:
    print(type(i), i)

s = 'aabfffbccddeeffghijwerwerewrwererewk'
c = 'abfcdef'
j = {2,1,3}
k = {3,2,1}
print('sets: ', j == k)
print(set(s), set(c))
print(set(s) >= set(c))
print('Valor da variavel __name__: ', __name__)

if __name__ == '__main__':
    print('Olaaaaaaaaa agora entendi o porque dessa linha kr... se estou executando é porque sou o arquivo principal!')