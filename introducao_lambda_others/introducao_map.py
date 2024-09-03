# INTRODUCAO MAP
numbers = [12,5,6,7,9,10,24,64]

squared = list(map(lambda x : x**2,numbers)) # define um lambda x, onde a condicao de x é x**2, agregando os valores de numbers como x, depois os listando com a funcao map
print(squared)

names = ["Ricardo", "Rogério", "Serjão", "Jurandir"]
names_upper = list(map(lambda x : x.upper(), names)) # cria uma funcao lambda que coloca em caixa alta todos os nomes da lista names
names_len_names = list(map(lambda x : len(x), names)) # funcao que mostra a quantidade de letras em cada nome
print(names_upper)
print(names_len_names)
