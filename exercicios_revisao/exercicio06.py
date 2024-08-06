# Exercício 06
# Nome: Fernando Gonçalves

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))

if(idade<16):
    print(f"{nome}, você não tem idade para votar")
elif(idade>=18 and idade<=65):
    print(f"{nome}, você é obrigado a votar na próxima votação")
elif(idade>=16 and idade<=17):
    print(f"{nome}, a escolha de votar é sua")