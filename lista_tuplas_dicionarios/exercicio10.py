# Exercício 10
# Nome: Fernando Gonçalves

agenda = []
contador = 0

while(contador<5):
    contador+=1
    pessoa = {}
    cpf = int(input("Digite seu CPF: "))
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    telefone = int(input("Digite seu telefone: "))

    pessoa["cpf"] = cpf
    pessoa["nome"] = nome
    pessoa["idade"] = idade
    pessoa["telefone"] = telefone
    agenda.append(pessoa)

print(f"Agenda com os dados de cinco pessoas: {agenda}")