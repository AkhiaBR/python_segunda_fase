# introducao a funcao

def inicio(): # define a funcao chamada inicio
    print("Minha primeira função! ") # tudo que a funcao vai executar uma vez chamada

inicio() # chama a funcao
#
def cores():
    cor1 = input("Digite uma cor: ")
    cor2 = input("Digite uma outra cor: ")
    print(f"As cores escolhidas foram: {cor1} e {cor2}")

cores()

# parametros

def nome(nickname): # a funcao so sera executada quando um valor for colocado em nickname ou seja, eu seu parametro
    print(f"Exemplo de um nome: {nickname}")

nome("Akhia") # printa o akhia e o toshi depois de chamados, repetindo a execucao da funcao
nome("Toshi")
#
def somar(a,b): # define uma funcao com multiplos parametros
    soma = a + b
    print(f"A soma de {a} + {b} é igual a {soma}")

somar(12,55)

# *args

def somar(*args): # cria uma funcao com um parametro indefinido, ou seja, nao importan quantos valores, ele sempre vai executar, armazenado-os em forma de tupla
    soma = 0
    for i in args:
        soma += i # a variavel soma vai ser igual a soma de todos os itens da variavel args que é um parametro indefinido

    print(f"O resultado da soma foi: {soma}") # print fora do for para nao ficar em um loop

somar(12,16,34,23,36,63,49)
#
def nomes(*n): 
    for i in range(len(n)):
        print(f"Nome: {n[i]}")

nomes("joao", "maria")
print("\n")

# kwargs

def pessoa(**dados):
    print(dados)
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

pessoa(nome="fernando", idade=17, cidade="morro da fumaca", altura=1.89)

# return

def somar(a,b):
    soma = (a + b)
    return soma

print(somar(12,5)) # para printar uma variavel de uma funcao fora da funcao, coloque escreva-a antes dos argumentos
#
def par(n):
    if(n%2==0): # Se o resto da divisão for zero o número é par
        return True # Par
    else:
        return False # Ímpar

numero = int(input("Digite um numero: "))
print(par(numero)) # printa se o numero colocado é true ou false (par ou impar)
#
def calculo(n1,n2):
    soma = (n1+n2)
    media = (soma/2)
    return soma, media # faz com que a funcao calculo() seja igual a soma e media juntas, já que retorna os valores de soma e media

soma_media = calculo(9,25)
print(soma_media)
#
def cadastro():
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    endereco = str(input("Digite seu endereço: "))
    return nome, idade, endereco

pessoa = cadastro() # pessoa recebe todos os valores que foram retornados na funcao cadastro
print(pessoa) # se pessoa é igual a cadastro, printa nome e endereco
#
def somar(a,b):
    global soma # com uma variavel do tipo global, voce consegue chamar ou printar essa variavel fora de uma funcao
    soma = a+b
    return soma

somar(5,7)
print(soma)

# funcoes em uma linha

def somar(a,b): return a+b
def multiplicar(a,b): return a*b

print(somar(5,7))
print(somar(2,8))

# bibliotecas
from datetime import * # importa todas as funcionalidades da biblioteca para o usar no codigo
from time import *
from math import *

data = date(2011, 11, 11) # declara uma variavel no formato ano, mes, dia (padrao USA)
print(data)
data_atual = date.today() # funcao do date que mostra a data do dia de hoje
print(data_atual)
ano = data_atual.year
print(ano)
mes = data_atual.month
print(mes)
dia = data_atual.day
print(dia)
#
print("Iniciando o código...")
sleep(2)
print("Bem vindo")
#
raiz = sqrt(144) # square root (raiz quadrada)
print(raiz)
potencia = pow(3,2) # potencia de 3 elevado na 2
print(potencia)
fatorial = factorial(4) # fatorial de 4
print(fatorial)