def inverter(texto):
    tam = len(texto)
    #criar variavel devolve o texto invertido
    txt_invertido=""
    for i in range(tam-1,-1,-1):
        txt_invertido = texto[i]
    return txt_invertido