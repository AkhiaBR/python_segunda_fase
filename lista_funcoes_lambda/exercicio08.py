# Exercício 08
# Nome: Fernando Gonçalves

from functools import reduce

lista_inteiros = [8,7,9,3,6]

inteiros_produto = reduce(lambda x,y : x*y, lista_inteiros)
print(f"Produto de todos os valores da lista: {inteiros_produto}")
