# Exercício 02
# Nome: Fernando Gonçalves

estado = True

def adicao():
    num1 = float(input("Digite o número: "))
    num2 = float(input("Digite o número que deseja somar: "))
    calculo = (num1+num2)
    print(f"Resultado da soma: {calculo}")
def subtracao():
    num1 = float(input("Digite o número: "))
    num2 = float(input("Digite o número que deseja diminuir: "))
    calculo = (num1-num2)
    print(f"Resultado da subtração: {calculo}")
def multiplicacao():
    num1 = float(input("Digite o número: "))
    num2 = float(input("Digite o número que deseja multiplicar: "))
    calculo = (num1*num2)
    print(f"Resultado da multiplicação: {calculo}")
def divisao():
    num1 = float(input("Digite o número: "))
    num2 = float(input("Digite o denominador: "))
    calculo = (num1/num2)
    print(f"Resultado da divisão: {calculo}")

while(estado==True):
    print("-------------------------------------")
    print("1- Adição")
    print("2- Subtração")
    print("3- Multiplicação")
    print("4- Divisão")
    print("-------------------------------------")
    escolha = int(input("Digite o número da operação que deseja realizar: "))

    if(escolha==1):
        adicao()
    elif(escolha==2):
        subtracao()
    elif(escolha==3):
        multiplicacao()
    elif(escolha==4):
        divisao()