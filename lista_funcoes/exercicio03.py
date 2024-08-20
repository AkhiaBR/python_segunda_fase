# Exercício 03
# Nome: Fernando Gonçalves

tarefas = []
estado = True

def adicionar():
    tarefa = str(input("Digite uma nova tarefa para sua lista de tarefas: "))
    tarefas.append(tarefa)
def remover():
    tarefa = str(input("Digite a tarefa que deseja remover da sua lista de tarefas: "))
    tarefas.remove(tarefa)
def atualizar():
    tarefa = str(input("Digite a tarefa que deseja modificar: "))
    tarefa_change = str(input("Digite a tarefa modificada: "))
    tarefas.remove(tarefa)
    tarefas.append(tarefa_change)
def visualizar():
    print(tarefas)

while(estado==True):
    print("-------------------------------------")
    print("1- Adicionar Tarefa")
    print("2- Remover Tarefa")
    print("3- Atualizar Tarefa")
    print("4- Visualizar Tarefa")
    print("-------------------------------------")
    escolha = int(input("Digite o número da opção que deseja executar: "))

    if(escolha==1):
        adicionar()    
    elif(escolha==2):
        remover()
    elif(escolha==3):
        atualizar()
    elif(escolha==4):
        visualizar()
