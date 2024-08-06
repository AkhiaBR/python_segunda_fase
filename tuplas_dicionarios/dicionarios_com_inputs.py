# Criação de dicionários com inputs
# Nome: Fernando Gonçalves

# Lista com dicionários
filmes = {}
nome = str(input("Nome do filme: "))
genero = str(input("Gênero do filme: "))

filmes["name"] = nome
filmes["genre"] = genero

print(filmes)
print("---------------------------")

# Lista com dicionários com inputs
locadora = []
contador = 0

while(contador<3):
    filmes = {} # O dicionário deve estar dentro do loop para que as chaves do dicionário "filmes" não sejam repetidas e substituídas
    contador += 1

    nome = str(input("Nome do filme: "))
    genero = str(input("Digite o gênero do filme: "))

    filmes["name"] = nome
    filmes["genre"] = genero

    locadora.append(filmes)

print(f"Lista de filmes da locadora: {locadora}")