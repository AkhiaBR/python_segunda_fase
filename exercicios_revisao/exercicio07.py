# Exercício 07
# Nome: Fernando Gonçalves

nome = str(input("Digite seu nome: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso/(altura*altura)

if(imc<18.5):
    print(f"{nome}, você está abaixo do peso")
elif(imc>=18.5 and imc<25):
    print(f"{nome}, você está com o peso normal")
elif(imc>=25 and imc<=30):
    print(f"{nome}, você está acima do peso")
elif(imc>=30):
    print(f"{nome}, você está obeso")