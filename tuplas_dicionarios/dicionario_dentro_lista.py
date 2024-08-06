# Execução do conteúdo aprendido
# Nome: Fernando Gonçalves

filmes = [ # Dicionário dentro de uma lista
    {"Nome":"Homem de Ferro", "Gênero":"Ação e Aventura"},
    {"Nome":"Meu Malvado Favorito", "Gênero":"Animação"},
    {"Nome":"Se Beber Não Case", "Gênero":"Comédia"}
]

print(filmes[0]["Gênero"])
print(filmes[2]["Gênero"])
print("---------------------------")
print(filmes[0].values())
print(filmes[2].keys())
print(filmes[1].items())

for i in filmes:
    print(i)

for i in filmes:
    for chave, valor in i.items():
        print(f"{chave}: {valor}")
