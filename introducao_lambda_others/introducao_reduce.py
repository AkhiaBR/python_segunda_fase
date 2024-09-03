# INTRODUCAO REDUCE
from functools import reduce # importa a funcao reduce da biblioteca functools

numbers = [5,7,12,9,1]

sum_numbers = reduce(lambda x,y : x+y,numbers) # pega os primeiros 2 valores da lista numbers e soma eles, fazendo isso para o resto dos numeros, indo de 2 em 2
print(sum_numbers)

max_numbers = reduce(lambda x,y : x if x>y else y, numbers) # o maior numero da lista só será maior se for maior que y, se ele nao for maior que y, ele se torna o y para o proximo x, ate encontrar o valor maximo
print(max_numbers)

min_numbers = reduce(lambda x,y : x if x<y else y, numbers) # o menor numero da lista