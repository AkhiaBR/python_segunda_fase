# Exercício 02
# Nome: Fernando Gonçalves

estado = True

def adicao():
    calculo = (num1+num2)
    print(f"Resultado da soma: {calculo}")
def subtracao():
    calculo = (num1-num2)
    print(f"Resultado da subtração: {calculo}")
def multiplicacao():
    calculo = (num1*num2)
    print(f"Resultado da multiplicação: {calculo}")
def divisao():
    calculo = (num1/num2)
    print(f"Resultado da divisão: {calculo}")

while(estado==True):
    print("-------------------------------------")
    print("1- Adição")
    print("2- Subtração")
    print("3- Multiplicação")
    print("4- Divisão")
    print("-------------------------------------")
    num1 = float(input("Digite algum número: "))
    num2 = float(input("Digite outro número: "))
    escolha = int(input("Digite o número da operação que deseja realizar: "))

    if(escolha==1):
        adicao()
    elif(escolha==2):
        subtracao()
    elif(escolha==3):
        multiplicacao()
    elif(escolha==4):
        divisao()