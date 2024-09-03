# Exercício 07
# Nome: Fernando Gonçalves

lista_inteiros = [2,3,7,11,23,52]

numeros_impares = list(filter(lambda x : x % 2 != 0, lista_inteiros))
print(f"Lista de números ímpares: {numeros_impares}")
print(f"Lista de números ímpares dobrados: {list(map(lambda x: x*2, numeros_impares))}")
