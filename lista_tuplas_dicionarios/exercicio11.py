# Exercício 11
# Nome: Fernando Gonçalves

contador = 0
pessoas = []

while(contador<2):
    contador+=1
    single_pessoa = {}
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    cpf = int(input("Digite seu CPF: "))

    single_pessoa["nome"] = nome
    single_pessoa["idade"] = idade
    single_pessoa["cpf"] = cpf
    pessoas.append(single_pessoa)

for i in pessoas:
    if(i["idade"]<18):
        print(f"Pessoas com menores de 18 anos: {i}")
        
if(i["idade"]>=18):
    print("Não há pessoas menores de 18 anos na lista")