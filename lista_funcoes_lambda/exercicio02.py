# Exercício 02
# Nome: Fernando Gonçalves

from functools import reduce

numbers = [2,2,2,2]
numbers_media = reduce(lambda x,y : x+y,numbers) # soma todos os elementos da lista
print(f"A lista {numbers} possui média de: {numbers_media/len(numbers)}") # soma da lista dividido pelo length da lista