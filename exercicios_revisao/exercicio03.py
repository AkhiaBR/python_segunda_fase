# Exercício 03
# Aluno: Fernando Gonçalves

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))

if(idade<2):
    print(f"{nome}, você está no bercário")
elif(idade>=3 and idade<=6):
    print(f"{nome}, você está no nível de Educação Infantil")
elif(idade>=7 and idade<=10):
    print(f"{nome}, você está no nível de Fundamental Nível I")
elif(idade>=11 and idade<=15):
    print(f"{nome}, você está no nível de Fundamental Nível II")
elif(idade>=16 and idade<=18):
    print(f"{nome}, você está no Ensino Médio")