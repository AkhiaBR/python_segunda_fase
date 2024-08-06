# Exercício 13
# Nome: Fernando Gonçalves

tarefas = []
contador = True

while(contador==True):
    print("------------------------------------------")
    print("1- Adicionar Tarefa")
    print("2- Remover Tarefa")
    print("3- Exibir Tarefa")
    print("4- Pesquisar")
    print("5- Sair do Programa")
    print("------------------------------------------")

    escolha = int(input("Digite o número desejado de acordo com o MENU exibido: "))

    if(escolha==1):
        tarefa = str(input("Digite sua próxima tarefa: "))
        tarefas.append(tarefa)
    elif(escolha==2):
        num = int(input("Digite o número da tarefa na lista de tarefas: "))
        tarefas.pop(num-1)
    elif(escolha==3):
        print(tarefas)
    elif(escolha==4):
        pesquisar = str(input("Digite a tarefa que deseja procurar: "))
        if(pesquisar in tarefas):
            print("Sua tarefa está presente na lista tarefas")
        else:
            print("Não foi possível encontrar sua tarefa")
    elif(escolha==5):
        selecao = str(input("Você tem certeza que deseja continuar? Sim (S) ou não (N): ")).upper()
        if(selecao=="S"):
            break
