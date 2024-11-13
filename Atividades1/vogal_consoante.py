letra = input("Digite uma letra:").lower()
if letra in "aeiou":
    print(f"A letra {letra} é uma vogal.")
elif letra.isalpha():
    print(f"A letra {letra} é uma consoante.")
else:
    print