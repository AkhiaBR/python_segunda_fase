# Introdução de Tuplas e Dicionários
# Aluno: Fernando Gonçalves

# Classificação das funções
tupla = ()
lista = []
string = "Arroz"
inteiro = 10
decimal = 1.5

print(type(tupla))
print(type(lista))
print(type(string))
print(type(inteiro))
print(type(decimal))

# Prova de que as funções abaixo são tuplas
tupla01 = ()
tupla02 = 1.6, "pão", True, 12

print("---------------------------")
print(type(tupla02))

# Acessando valores das tuplas
print("---------------------------")
print(tupla02[:-1]) # Acessa o último valor da tupla
print(tupla02[:2]) # Acessa os dois primeiros itens da tupla
print(tupla02[:-2]) # Acessa o último e o penúltimo item da tupla (abaixo da posição 0, o acesso é puxado do último item da tupla, sendo o item -1)
print(tupla02[-2:]) # Acessa o penúltimo e o último item da tupla

# Comprimento da tupla
print("---------------------------")
print(len(tupla02))

# Concatenação de tuplas
tupla_concatenada = tupla01 + tupla02

print("---------------------------")
print(tupla_concatenada)

# Replicação da tupla
tupla_replicada = tupla02*2

print("---------------------------")
print(tupla_replicada)

# Mínimo e máximo
tupla_numerica = (1000, 500, 000)

print("---------------------------")
print(max(tupla_numerica))
print(min(tupla_numerica))

# Percorrendo valores da tupla
tupla_for = (100, 50, 10)
print("---------------------------")

for i in tupla_for:
    print(f"Valores: {i}") # Retorna todos os itens da tupla

print("---------------------------")

for i in range(len(tupla_for)): # Retorna quantas posições existem na tupla
    print(i)

# Desempacotamento
tupla_coordenada = (5,7)
variavel_x, variavel_y = tupla_coordenada

print("---------------------------")
print(type(tupla_coordenada))
print(variavel_x)
print(variavel_y)

tupla_idades = (10, 12, 16, 18)
idade01, idade02, idade03, idade04 = tupla_idades

print("---------------------------")
print(idade01)
print(idade02)
print(idade03)
print(idade04)

# Função enumerate
tupla_frutas = ("maca", "melancia", "banana", "pessego")

for index, i in enumerate(tupla_frutas, start=1): # Enumera a tupla começando a contagem do 1 e não do 0 com o "start=1"
    print(f"A fruta {i} está na posição: {index}")
