# Exercício 05
# Nome: Fernando Gonçalves

lista_numbers = [2,5,6,10,20]

numbers_divisiveis = list(filter(lambda x : x % 5 == 0,lista_numbers)) # se o resto de x/5 for igual a 0, ele é divisível por 5
print(f"Números da lista que são divisívies por 5: {numbers_divisiveis}")