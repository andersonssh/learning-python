def processInput(entrada):
    itens = {}
    linhas = [linha for linha in entrada.split('\n') if linha != '\n']
    # pega somente as linhas dos itens e precos
    for linha in linhas[2:-1]:
        item, preco = linha.split(' ')
        itens[item] = int(preco.replace(',', '.'))

    total = sum(itens.values())
    pagamento_individual = sum(
        [itens[nome_item] for nome_item in itens.keys() if nome_item not in linhas[-1].split(' ')]) // int(
        linhas[0])
    sobra = total - pagamento_individual * int(linhas[0])
    saida = f'{total}\n{pagamento_individual}\n{sobra}'
    return saida


print(processInput("""6
4
entrada 150
bebidas 60
principal 240
sobremesa 30
entrada bebidas sobremesa"""))
