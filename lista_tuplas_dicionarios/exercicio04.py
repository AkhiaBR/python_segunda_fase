# Exercício 04
# Nome: Fernando Gonçalves

contador = 0
numeros = []
numeros_pares = []

while(contador<4):
    contador+=1
    num = int(input("Digite algum número: "))
    numeros.append(num)

tupla_num = tuple(numeros) # transforma a lista numeros em tupla
contador9 = tupla_num.count(9) # conta quantas vezes o numero 9 aparece em tupla_num

if(contador9):
    print(f"Vezes em que o número nove apareceu na tupla: {contador9}") 
else:
    print("Nenhum número 9 foi encontrado na tupla")

if(3 in tupla_num):
    posicao3 = tupla_num.index(3)+1 # pega o index (posicao) do numero 3 e adiciona por 1 para comecar a contar do um
    print(f"Posição do número três na tupla: {posicao3}")
else:
    print("O número três não foi digitado")

for i in tupla_num:
    if(i%2 == 0):
        numeros_pares.append(i)

if(numeros_pares): # confirma se tem valores lista de numeros_pares
    print(f"Números que são pares da tupla: {numeros_pares}")
else:
    print("Nenhum número par encontrado na tupla")
