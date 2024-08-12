# Exercício 03
# Aluno: Fernando Gonçalves

import random

contador = 0
num_aleatorios = []
tupla_aleatorios = ()

while(contador<5):
    contador+=1
    num_aleatorios.append(random.randint(1,100)) # O random.randint gera um número de 1 a 100, random de randomizar e randint é como se fosse um range

tupla_aleatorios = tuple(num_aleatorios) # tuple transforma os itens da lista em itens de tupla

print(f"Tupla de cinco números aleatórios: {tupla_aleatorios}")
print(f"Maior valor da tupla: {max(tupla_aleatorios)}")
print(f"Menor valor da tupla: {min(tupla_aleatorios)}")