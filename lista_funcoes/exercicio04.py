# Exercício 04
# Nome: Fernando Gonçalves

status = True
contatos = []

def adicionar():
    contato = str(input("Digite o nome do contato que deseja adicionar: "))
    for i in contatos: # checa se o contato novo já é um existente na lista
        if(i==contato):
            print("Contato já adicionado à lista")
    contatos.append(contato)

def visualizar():
    print(f"Sua lista de contatos: {sorted(contatos)}")

def editar():
    contato = str(input("Digite o contato que deseja editar: "))
    if contato in contatos: # se o contato a ser mudado estiver na lista:
        posicao = contatos.index(contato) # a posicao do contato antigo que deseja editar é o index do contato antigo na lista
        novo_contato = str(input("Digite o novo nome do contato: "))
        contatos[posicao] = novo_contato # o index do contato antigo recebera um update do novo contato, substituindo-o
    else:
        print("O contato que você deseja editar não existe dentro da lista")

def excluir():
    contato = str(input("Digite o nome do contato que deseja excluir: "))
    if contato in contatos: # checa se há um contato com o mesmo nome existente usando IF
        contatos.remove(contato)
    else:
        print("Não há nenhum contato com esse nome na lista, tente novamente ")


while(status==True):
    print("______________________")
    print("1- Adicionar Contato")
    print("2- Visualizar Contato")
    print("3- Editar Contato")
    print("4- Excluir Contato")
    print("______________________")
    escolha = int(input("Digite o número da opção desejada no menu: "))

    if(escolha==1):
        adicionar()
    elif(escolha==2):
        visualizar()
    elif(escolha==3):
        editar()
    elif(escolha==4):
        excluir()
