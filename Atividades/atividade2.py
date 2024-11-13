numeros = []
for _ in range(0,5):
    numero = int(input("Digite um numero: "))
    numeros.append(numero)
    
#variavel d a soma
soma = sum(numeros)
média = soma / 5

print(f"Soma: {soma}")
print(f"Media: {média}")