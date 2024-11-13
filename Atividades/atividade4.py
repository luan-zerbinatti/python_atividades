numeros = []
n1  = int(input("Digite o primeiro numero "))
n2 = int(input("Digite o segundo numero "))
n3 = int(input("Digite o terceiro numero"))
n4 = int(input("Digite o quarto numero"))
n5 = int(input("Digite o quinto numero"))


numeros.append(n1)
numeros.append(n2)
numeros.append(n3)
numeros.append(n4)
numeros.append(n5)
maior = numeros[0]
for n in numeros:
    if n > maior:
        maior = n
print("o maior numero é",maior)