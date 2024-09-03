# INTRODUCAO
print((lambda x : x**2) (8)) # define um lambda, ou seja, uma funcao em que o x é igual a x^2, depois agrega o valor de 8 em x

def quadrado(x): # mostra que podemos fazer a mesma coisa do lambda com uma funcao
    return x**2
print(quadrado(8))

quadrado_lambda = lambda x : x**2 # variaveis com lambdas
print(quadrado_lambda(8))

# UTILIZANDO LAMBDA
lista = [
    lambda x : x*2,
    lambda x : x**2,
    lambda x : x**3
]

for i in lista: # para os itens da lista (lambda), agrege o valor de 5, ou seja, x = 5
    print(i(5))

value = int(input("Digite um valor: ")) # faz a mesma coisa que o comando anterior, podendo mudar a variavel x
for i in lista:
    print(i(value))

name_age = lambda x,y : print(f"{x}, possui {y} anos") # agrega valores de nome e idade cadastrados pelo usuário
name = str(input("Digite um nome: "))
age = int(input("Digite sua respectiva idade: "))
name_age(name,age) # agrega os valores no lambda

(lambda x,y : print(f"{x}, possui {y} anos")) (str(input("Digite seu nome: "))),(int(input("Digite sua idade: "))) # executa uma funcao lambda em somente uma linha, fazendo o mesmo que: (lambda x,y : print(...) (condicaoX),(condicaoY))
