# Exercício 03
# Nome: Fernando Gonçalves

lista_nomes = ["Ricardo", "Jurandir", "Carlão", "Roberto"]

nomes_a = list(filter(lambda x : "a" in x,lista_nomes))
print(f"Nomes que possuem a letra A em sua composição: {nomes_a}")