def busca_linear(lista, valor):
    for i, item in enumerate(lista):
        if item == valor:
            return i
    return -1
