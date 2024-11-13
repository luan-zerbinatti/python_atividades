def soma(n1,n2):
    return n1 + n2

def produto(n1,n2):
    return n1 * n2

def restoDivisao(n1, n2):
    return n1 % n2

def separarResultados(texto):
    print("------------- O resultado de " +texto+"------------------")
    
    print("Ola, Seja bem vindo ao programa de calculos")
    separarResultados("Multiplicação")
    print("Entre os numeros 5 e 10 é " +str(produto(5,10)))
    separarResultados("Resti da divisão")
    print("Entre os numeros 5 e 10 é " +str(restoDivisao(5,10)))