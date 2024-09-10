# Exercício 11
# Nome: Fernando Gonçalves

lista_palavras = ["Abobora", "Banana", "Pão","Carreta", "Dark Souls"]

palavras_3 = list(filter(lambda x : len(x)>3,lista_palavras))
print(f"Lista de palavras com mais de três letras: {palavras_3}")

numero_letras_funcao = list(map(lambda x : len(x),palavras_3))
print(f"Número de letras em cada palavra: {numero_letras_funcao}")