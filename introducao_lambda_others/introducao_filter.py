# INTRODUCAO FILTER
numbers = [4,5,8,9,10]

numbers_pares = list(filter(lambda x : x % 2 == 0, numbers)) # agrega os numeros da lista na funcao lambda, filtrando quais sao pares pela logica(lambda x : x & 2 == 0) e posteriormente os listando 
print(numbers_pares)

names = ["Mariane", "Sabrina", "Alice", "Pedro"]

names_a = list(filter(lambda x : "a" in x,names)) # verifica nomes que contem a em sua composicao
print(names_a) 