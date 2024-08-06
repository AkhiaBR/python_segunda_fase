# Exercício 05
# Nome: Fernando Gonçalves

print("MENU das Formas de pagamento: ")
print("------------------------")
print("1- À vista no dinheiro")
print("2- À vista no cartão")
print("3- 2x sem juros")
print("4- 3x com juros")
print("------------------------")

produto = str(input("Digite o nome do produto: "))
quantidade = int(input("Qual a quantidade desse produto: "))
preco = float(input("Digite o preço desse produto: "))
forma_pagamento = int(input("Digite o número referente à forma de pagamento presente no MENU: "))
total = (preco*quantidade)

if(forma_pagamento==1):
    print(f"Você pagará {total-(total*0.10)} reais comprando {produto}")
elif(forma_pagamento==2):
    print(f"Você pagará {total-(total*0.05)} reais comprando {produto}")
elif(forma_pagamento==3):
    print(f"Você pagará {total/2} em cada parcela comprando {produto}")
elif(forma_pagamento==4):
    print(f"Você pagará {(total+(total*0.05))/3} em cada parcela comprando {produto}")
