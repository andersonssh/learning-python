def to_camel_case(text):
    if len(text) == 0:
        return ''
    novo_texto = text.replace('-', ' ').replace('_', ' ')
    print(novo_texto)
    lista = [i.capitalize() for i in novo_texto.split('_')]
    if text[0].islower():
        lista[0] = lista[0][0].lower() + lista[0][1:]

    return ''.join(lista)

print(to_camel_case('seila-Tio_Zau'))