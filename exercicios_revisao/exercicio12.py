# Exercício 12
# Nome: Fernando Gonçalves

nome = str(input("Digite o seu nome: "))
idade = int(input("Digite a sua idade: "))
valor_plano = float(input("Digite o valor do seu plano de saúde: "))

if(idade<=18):
    valor_real = valor_plano+(valor_plano*0.05)
elif(idade>=19 and idade<=35):
    valor_real = valor_plano+(valor_plano*0.10)
elif(idade>=36 and idade<=60):
    valor_real = valor_plano+(valor_plano*0.15)
elif(idade>60):
    valor_real = valor_plano+(valor_plano*0.20)

print(f"{nome}, seu valor do plano será renovado para: {valor_real} reais")