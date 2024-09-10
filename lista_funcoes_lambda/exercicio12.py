# Exercício 12
# Nome: Fernando Gonçalves

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