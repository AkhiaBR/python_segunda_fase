# Exercício 08
# Nome: Fernando Gonçalves

pessoa = {}
nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
telefone = int(input("Digite seu telefone: "))
endereco = str(input("Digite seu endereço: "))

pessoa["nome"] = nome
pessoa["idade"] = idade
pessoa["telefone"] = telefone
pessoa["endereco"] = endereco

print(f"O nome da pessoa é: {pessoa['nome']}")