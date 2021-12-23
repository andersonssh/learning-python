# Escreva uma função que receba uma string de uma ou mais palavras e retorne a mesma string, mas com todas as palavras de cinco ou mais letras invertidas (assim como o nome deste Kata). As strings passadas consistirão apenas em letras e espaços. Os espaços serão incluídos apenas quando mais de uma palavra estiver presente.

# Exemplos: spinWords ("Ei companheiros guerreiros") => retorna "Ei soriehnapmoc sorierreug" spinWords ("Isto é um teste") => retorna "Isto é um teste" spinWords ("Este é outro teste") => retorna "Isto é o ortuo etset"

# minha solucao
def spin_words(sentence):
    return ' '.join([i[::-1] if len(i) > 4 else i for i in sentence.split(' ')])

# melhor solucao da platforma

def spin_words2(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])