# Exercício 1

from functools import reduce

lista_numeros = [2,5,6,2,6,7]

num_pares = list(filter(lambda x : x % 2 == 0,lista_numeros))
print(f"A lista {lista_numeros}, possui os números pares: {num_pares}")

# Exercício 2

lista_numeros = [2,2,2,2]

num_media = reduce(lambda x,y : x+y,lista_numeros)
print(f"A lista {lista_numeros}, possui média de: {num_media/len(lista_numeros)}")

# Exercício 3

lista_nomes = ["Fernando", "Cassio", "Flávio"]

nomes_f = list(filter(lambda x : "F" in x[0],lista_nomes))
print(f"Nomes que começam com a letra F: {nomes_f}")

# Exercício 4

lista_num = [2,5,10]

num_square = list(map(lambda x : x**2,lista_num))
print(f"A lista {lista_num} ao quadrado é: {num_square}")

# Exercício 5

lista_num = [2,5,25,50]

div_cinco = list(filter(lambda x : x % 5 == 0,lista_num))
print(f"Número divisíveis por cinco: {div_cinco}")

# Exercício 7

lista_num = [2,5,8,13]

dobrados_imp = list(map(lambda x : x*2 if x % 2 != 0 else x,lista_num))
print(f"Lista de número ímpares dobrados e pares normais: {dobrados_imp}")

# Exercício 8

lista_num = [2,3,5,6,7]

prod_num = reduce(lambda x,y : x*y,lista_num)
print(f"Produto da lista de números: {prod_num}")

# Exercício 10

lista_c = [30,80,120]

temp_f = list(map(lambda x : (x*9/5)+32,lista_c))
print(f"Lista convertida para Fahrenheit: {temp_f}")

# Exercício 11

lista_pal = ["Fernando", "Cassio", "Joao", "Nu"]

mais_tr = list(filter(lambda x : len(x)>3,lista_pal))
num_car = list(map(lambda x : len(x),mais_tr))

print(f"Palavras com mais de três letras: {mais_tr}, número de caracteres dessas palavras: {num_car}")

# Exercício 12

def calculo_cust(lista_pre,valor_per):
    pre_desc = list(map(lambda x : x - x*valor_per/100,lista_pre))
    print(f"O valor da compra com desconto aplicado é: {pre_desc}")

lista_pre = [20,50,80,100]
valor_per = 20

if(len(lista_pre)>3):
    calculo_cust(lista_pre,valor_per)
else:
    print(f"Valor da compra: {sum(lista_pre)}")

# Exercício 13

def aumento(funcionarios):
    func_2000 = dict(filter(lambda x : x[1]>2000,funcionarios.items()))                     # usa x[1] porque o comando funcionarios.items() transforma os valores em tuplas ("Fernando",3000); x[1] = 3000
    apl_aumen = dict(map(lambda x : (x[0], x[1]+x[1]*10/100),func_2000.items()))            # x[0] (nome) e x[1] (salário)
    print(f"Funcionários com salário maior que R$ 2000: {func_2000}, valores atualizados: {apl_aumen}")

funcionarios = {
    "Fernando":3000,
    "Cassio":1800,
    "Flávio":2400
}

aumento(funcionarios)
