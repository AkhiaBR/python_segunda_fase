# Exercício 06
# Nome: Fernando Gonçalves

contador_prestacoes = 0 # conta prestacoes
prestacoes_total = [] # armazena os precos das prestacoes

def valor_pagamento(p,a): # funcao que calcula o valor real da prestacao
    if(a==0 or a<0): # se nao houver atraso, multa inexistente
        multa = 0
    else:
        multa = 0.03
    juros = (a*0.001) # juros multiplicado por dia de atraso
    total = dinheiro+(dinheiro*multa)+(dinheiro*juros) # equacao do valor real da prestacao
    prestacoes_total.append(total) # armazena o valor real na lista com as outras prestacoes
    return(total) # retorna o valor total para a funcao

while(True): # cria o loop
    print("___________________")
    escolha = str(input("Deseja pagar suas prestações? Sim(S) ou Não(N): ")).upper()
    print("___________________")

    if(escolha=="S"): 
        dinheiro = float(input("Digite o valor a ser pago nessa prestação: ")) # preco bruto da prestacao
        if(dinheiro==0): # se o preco for 0, encerra
            break
        atraso = int(input("Digite os dias em atraso da prestação (coloque zero se nenhum): ")) 
        total = valor_pagamento(dinheiro, atraso) # coloca os valores que a funcao precisa para calcular
        contador_prestacoes+=1 # adiciona mais uma quantidade de prestacoes
        print(f"O valor a ser pago nessa prestação é: {total}") 
    elif(escolha=="N"):
        break
    else:
        print("Valor errado, tente novamente")

print("___________________")
print(f"Relatório das prestações pagas hoje: Quantidade de Prestações: {contador_prestacoes}, Valor total das prestações: {sum(prestacoes_total)}")