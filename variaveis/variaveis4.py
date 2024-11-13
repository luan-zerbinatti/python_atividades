alimentos = ["Maçã","Arroz","Feijão"]
categoria = ("Grãos","Frutas","Legumes")
pessoa = {"Nome":"Paula","Idade":"38","Altura":"1.65"}
          
print(alimentos)
print(type(alimentos))
print(len(alimentos)) 
# adcionar mais um elemento
alimentos.append("Macarrão")
print(alimentos)
print(len(alimentos))


print(categoria)
print(type(categoria))
print(len(categoria))

print(pessoa)
print(type(pessoa))
print(len(pessoa)) 
# Adcionar um item a pessoa
# Adcionar uma nova chave como seu respectivo valor
# esta sendo adcionado a chave email com o valor
# email da pessoa
pessoa["email"]="paula@gmail.com"
print(pessoa)
print(len(pessoa))     