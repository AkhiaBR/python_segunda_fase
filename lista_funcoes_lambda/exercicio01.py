# Exercício 01
# Nome: Fernando Gonçalves

numeros = [2,6,4,9,12,3,54]

numeros_pares = list(filter(lambda x : x % 2 == 0,numeros))
print(f"Números pares da lista: {numeros_pares}")
