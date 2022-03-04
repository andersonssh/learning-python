def decrescente(lista: list) -> list:
    """
    Organiza lista de números em ordem decrescente

    Args:
        lista: lista de numeros
    Returns:
        list: retorna lista
    """
    organizado = False
    while not organizado:
        organizado = True
        for i in range(0, len(lista) - 1):
            if lista[i] < lista[i + 1]:
                organizado = False
                lista[i], lista[i + 1] = lista[i + 1], lista[i]

    return lista


if __name__ == '__main__':
    decrescente([1, 2, 3, 4, 5])
