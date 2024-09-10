# Exercício 12
# Nome: Fernando Gonçalves

# Imagine que você está trabalhando em um sistema de e-commerce que aplica descontos
# progressivos com base na quantidade de produtos comprados. Crie uma função que receba uma
# lista de preços e um valor de desconto percentual. A função deve usar map() e lambda para
# aplicar o desconto a cada item e retornar uma nova lista com os preços atualizados.

produtos = {}
contador = 0

def desconto():
    desconto_funcao = list(map(lambda x : x.values-x.values()*0.5,produtos))
    return desconto_funcao

quantidade = int(input("Digite a quantidade de produtos que deseja comprar: "))

while(contador<quantidade):
    produto = str(input("Digite o nome do produto desejado: "))
    valor = float(input("Digite o valor desse produto: "))
    produtos[produto] = valor

    if(quantidade>=3):
        desconto()
        print(f"O valor final da compra será: {desconto_funcao}")
    else:
        print(f"O valor final da compra será: {sum(produtos.values())}")