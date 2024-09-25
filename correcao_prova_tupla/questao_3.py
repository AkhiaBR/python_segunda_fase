# questão 3 - Fernando Gonçalves / 2190

tarefas = {}

def adicionar():
    tarefa = str(input("Escreva qual a tarefa a ser feita: "))
    tarefas[len(tarefas)+1] = tarefa

def alterar():
    cod_tarefa = int(input("Digite o código da tarefa que deseja alterar: "))
    op = str(input("Você deseja alterar o código (C), ou a descricação da tarefa (D): ")).upper().strip()
    if(op=="C"):
        nov_cod = int(input("Digite o novo código da tarefa: "))
        tarefas[nov_cod] = tarefas[cod_tarefa] # faz com que os values das chaves sejam os mesmos
        del tarefas[cod_tarefa] # deleta a chave antiga
    elif(op=="D"):
        nov_tar = str(input("Digite nova descrição da tarefa: "))
        tarefas[cod_tarefa] = nov_tar

def excluir():
    cod_tarefa = int(input("Digite o código da tarefa que deseja excluir: "))
    if(cod_tarefa in tarefas.keys()):
        del tarefas[cod_tarefa]
    else:
        print("ERRO: Tarefa não existente. Tente novamente...")

def pesquisar():
    print(f"Lista geral de tarefas cadastradas: {tarefas}")
    print(f"Lista em ordem numérica: {sorted(tarefas.values())}")


while True:
    print("_______________________________")
    print("1 - Adicionar Tarefa")
    print("2 - Alterar Tarefa")
    print("3 - Excluir Tarefa")
    print("4 - Pesquisar Tarefa")
    print("5 - Sair")
    print("_______________________________")
    op = int(input("Digite o número referente à opção desejada no menu: "))

    if(op==1):
        adicionar()
    elif(op==2):
        alterar()
    elif(op==3):
        excluir()
    elif(op==4):
        pesquisar()
    elif(op==5):
        break
    else:
        print("ERRO: Valor inserido inválido. Tente novamente...")