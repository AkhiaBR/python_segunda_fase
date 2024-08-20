# Exercício 01
# Aluno: Fernando Gonçalves

from math import *

estado = True

def circulo():
        raio = float(input("Digite o raio do círculo: "))
        pi = 3.14
        area = pi*pow(raio,2)
        print(f"A área do círculo é: {area}")
def retangulo():
        base = float(input("Digite a base do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        area = base*altura
        print(f"A área do retângulo é: {area}")
def triangulo():
        base = float(input("Digite a base do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        area = (base*altura)/2
        print(f"A área do triângulo é: {area}")

while(estado==True):
    print("-------------------------------------")
    print("1- Círculo")
    print("2- Retângulo")
    print("3- Triângulo")
    print("-------------------------------------")
    escolha = int(input("Digite o número da forma que deseja calcular: "))

    if(escolha==1):
        circulo()
    elif(escolha==2):
        retangulo()
    elif(escolha==3):
        triangulo()