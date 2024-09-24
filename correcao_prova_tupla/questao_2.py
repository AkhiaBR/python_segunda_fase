# questão 2

funcionarios = {}
total_funcionarios = 0

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

def excluir():
    cod_funcionario = int(input("Digite o código do funcionário que deseja excluir os valores: "))
    op = str(input("O que você deseja excluir? Nome (N) ou cargo (C): ")).upper().strip()
    lista_excluir = funcionarios[cod_funcionario] # cria uma copia da lista dos funcionários principais
    if(op=="N"):
        lista_excluir[0] = "NULO" # altera o valor da lista cópia
        funcionarios[cod_funcionario] = lista_excluir # cola a cópia na lista original
    elif(op=="C"):
        lista_excluir[1] = "NULO"
        funcionarios[cod_funcionario] = lista_excluir

def pesquisar():
    print(f"Lista completa de funcionários: {funcionarios}")
    print(f"Lista completa de funcionários em ordem alfabética: {sorted(funcionarios)}")
    print(f"Total de funcionários cadastrados: {total_funcionarios}")


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
        total_funcionarios += 1
        cadastrar()
    elif(op=="A"):
        alterar()
    elif(op=="E"):
        excluir()
    elif(op=="P"):
        pesquisar()
    elif(op=="S"):
        break
    else:
        print("ERRO: Valor inserido errado. Digite novamente um novo valor...")