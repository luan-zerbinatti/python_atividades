# Exercicio 1 Funcões
def soma(num1,num2):
    return num1 + num2
 
# Exercicio 2 Funções
def converterCelfah(tempCelsius):
    fah = 1.8 * tempCelsius + 32
    return fah
 
# Exercicio 3 Funcões
def parImpar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"
   
# Exercicio 4 Funções
def inverter(texto):
    tam = len(texto)
    # criar variavel que devolve o textp invertido
    txt_invertido =""
    for i in range(tam-1,-1,-1):
        txt_invertido = texto[i]
    return txt_invertido
 
# Exercicio 5 Funções
def palindromo(palavra):
    palavra = palavra.lower()
    cp_palavra = palavra.lower()
    if cp_palavra==inverter(palavra):
        return "È um palindromo"
    else:
        return "Não é um palindromo"
   
# Exercicio 6 Funções
def media(lista_numeros):
    resultado = 0
    for i in  lista_numeros:
        resultado += i
    return resultado / len(lista_numeros)
 
# Exercicio 7 Funções
 
def lista_pares(lista_numeros):
    lst_pares = []
    for i in lista_numeros:
        if i % 2 == 0:
            lst_pares.append(i)
    return lst_pares        
   
