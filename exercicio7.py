def lista_pares(lista_numeros):
    lst_pares = []
    for i in lista_numeros:
        if i % 2 == 0:
            lst_pares.append(i)
    return lst_pares