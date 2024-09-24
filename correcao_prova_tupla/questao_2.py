# questão 2

funcionarios = {}

def cadastrar():
    funcionario_lista = []

    nome = str(input("Digite o nome do funcionário: "))
    cargo = str(input("Digite o cargo desse funcionário: "))

    funcionario_lista.append(nome)
    funcionario_lista.append(cargo)
    funcionarios[len(funcionarios)+1] = funcionario_lista

def alterar():
    cod_funcionario = int(input("Qual o código do funcionário que deseja alterar?: "))
    op = str(input("O que você deseja alterar? Nome (N) ou cargo (C): ")).upper().strip()
    if(op=="N"):
        nome_ant = str(input("Digite o nome do funcionário que deseja alterar: "))
        nome = str(input("Digite o novo nome do funcionário: "))
        for i in funcionarios[cod_funcionario]:
            if(i==nome):
                print("ERRO: Valor já inserido. Tente novamente...")
        else:
            index_nome_ant = funcionarios[cod_funcionario].index(nome_ant) # pega o index do nome que o usuário deseja alterar
            funcionarios[cod_funcionario][index_nome_ant] = nome
    elif(op=="C"):
        cargo_ant = str(input("Digite o cargo do funcionário que deseja alterar: "))
        cargo = str(input("Digite o novo cargo do funcionário: "))
        for i in funcionarios[cod_funcionario]:
            if(i==cargo):
                print(f"ERRO: Valor já inserido. Tente novamente...")
        else:
            index_cargo_ant = funcionarios[cod_funcionario].index(cargo_ant)
            funcionarios[cod_funcionario][index_cargo_ant] = cargo

# def excluir():
def pesquisar():
    print(funcionarios)

while True:
    print("___________________________")
    print("C - Cadastrar")
    print("A - Alterar")
    print("E - Excluir")
    print("P - Pesquisar")
    print("S - Sair")
    print("___________________________")
    op = str(input("Digite a letra referente à opção desejada no menu superior: ")).upper().strip()

    if(op=="C"):
        cadastrar()
    elif(op=="A"):
        alterar()
    # elif(op=="E"):
    #     excluir()
    elif(op=="P"):
        pesquisar()
    elif(op=="S"):
        break
    else:
        print("ERRO: Valor inserido errado. Digite novamente um novo valor...")