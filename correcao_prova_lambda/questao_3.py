# questão 3 - Fernando Gonçalves / 2190

pedidos = {}

def adicionar():
    pratos = []
    nome = str(input("Digite o nome do cliente: "))
    prato = str(input("Digite o pedido do cliente: "))
    while True:
        op = str(input("Deseja cadastrar mais pedidos para o cliente?: S/N: ")).upper().strip()
        if(op=="N"):
            pratos.append(prato)
            pedidos[nome] = pratos
            break
        else:
            prato2 = str(input("Digite o pedido do cliente: "))
            pratos.append(prato)
            pratos.append(prato2)
            pedidos[nome] = pratos

def atualizar():
    nome = str(input("Digite o nome do cliente que deseja atualizar: "))
    if nome in pedidos:
        prato_antigo = str(input("Digite o prato que deseja alterar: "))
        
        if prato_antigo in pedidos[nome]:
            novo_prato = str(input("Digite o novo pedido: "))
            index = pedidos[nome].index(prato_antigo)
            pedidos[nome][index] = novo_prato # atualiza o pedido com o index do nome fornecido
        else:
            print("Pedido não encontrado")
    else:
        print("Cliente não encontrado")

def remover():
    nome = str(input("Digite o nome do cliente que deseja remover o pedido: "))
    if nome in pedidos:
        prato = str(input("Digite o pedido a ser removido: "))
        if prato in pedidos[nome]:
            index = pedidos[nome].index(prato)
            pedidos[nome].pop(index)  # remove o pedido utilizando o indx
        else:
            print("Pedido não encontrado.")
    else:
        print("Cliente não encontrado.")

def filtrar():
    nome = str(input("Digite o nome do cliente que deseja filtrar: "))
    if nome in pedidos:
        print(f"O cliente {nome} possui os pedidos: {pedidos[nome]}")
    else:
        print("ERRO: Cliente não encontrado. Tente novamente...")

def visualizar():
    print(sorted(pedidos.items()))

while True:
    print("__________________")
    print("1- Adicionar Pedidos")
    print("2- Atualizar Pedidos")
    print("3- Remover Pedidos")
    print("4- Filtrar Pedidos")
    print("5- Visualizar Pedidos")
    print("6- Encerrar Programa")
    print("__________________")
    op = int(input("Digite o número da opção referente ao menu: "))

    if(op==1):
        adicionar()
        print(pedidos)
    elif(op==2):
         atualizar()
    elif(op==3):
        remover()
    elif(op==4):
        filtrar()
    elif(op==5):
        visualizar()
    elif(op==6):
        print("Encerrando o programa...")
        break