# Introdução de Dicionários 
# Nome: Fernando Gonçalves

# Valores dos dicionários
carros = {"marca":"chevrolet", "modelo":"onix", "ano":2020,}

print(carros)

# Acessando dados dos dicionários tradicionalmente
print("---------------------------") # Se não haver valor ou chave, o código ficará com erro
print(carros["marca"])
print(carros["ano"])

# Acessando dados dos dicionários com o "get()"
print("---------------------------") # Se não haver valor ou chave, o console mostrará "none", tendo a opção de colocar uma mensagem de erro se o valor ou chave não existir
print(carros.get("marca", "Chave inexistente"))
print(carros.get("ano", "Chave inexistente"))
print(carros.get("cor", "Chave inexistente"))

# Acessando somente as chaves do dicionário
print("---------------------------")
print(carros.keys())

# Acessando somente os valores do dicionário
print("---------------------------")
print(carros.values())

# Acessando as chaves e valores do dicionário
print("---------------------------")
print(carros.items())

# Adicionando ou alterando itens no dicionário
carros["ano"] = 2015
carros["placa"] = "AQG1M45"

print("---------------------------")
print(carros.items())

# Deletando itens no dicionário com o "pop()"
carros_pop = carros.pop("placa")

print("---------------------------")
print(carros_pop)
print(carros.items())

# Deletando itens no dicionários com o "delete"
del carros["placa"]

print("---------------------------")
print(carros.items())

# Verificando itens no dicionário
print("---------------------------")
print("placa" in carros)

# Verificando se o valor de um item está no dicionário
print("---------------------------")
print("onix" in  carros.values())
print("tracker" in carros.values())

# Iterando sobre um dicionário
for i in carros: # Retorna as chaves
    print(i)

for i in carros.values(): # Retorna os valores das chaves
    print(i)

for chave, valor in carros.items():
    print(f"{chave}:{valor}") # Retorna o nome da chave e o valor