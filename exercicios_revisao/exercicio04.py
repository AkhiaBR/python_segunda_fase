# Exercício 04
# Aluno: Fernando Gonçalves

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
peso = float(input("Digite o valor de seu peso: "))

if(idade<15):
    print(f"Você está abaixo da idade padrão para doar sangue")
elif(idade>=16 and idade<=17 and peso>55):
    print(f"Você precisa de autorização dos pais ou responsáveis")
elif(idade>=18 and idade<=69 and peso>60):
    print(f"Você está apto a ser doador de sangue!")
elif(idade<15):
    print(f"Você está acima da idade padrão para doar sangue")