# Exercício 13
# Nome: Fernando Gonçalves

funcionarios = {}
estado = True

while(estado==True):
    print("-----------------------")
    print("C- Cadastrar")
    print("E- Excluir")
    print("P- Pesquisar")
    print("S- Sair")
    print("-----------------------")
    escolha = str(input("Digite a letra da opção que deseja executar: ")).upper()

    if(escolha=='C'):
        nome = str(input("Digite o nome do funcionário: "))
        cargo = str(input("Digite o cargo desse funcionário: "))
        funcionarios[nome] = cargo
    elif(escolha=='E'):
        chave_deletar = str(input("Digite o nome do funcionário que deseja deletar: "))
        if(chave_deletar in funcionarios):
            print("Funcionário removido com sucesso!")
            del funcionarios[chave_deletar]
        else:
            print("Funcionário não encontrado. DICA: Verifique se o nome foi digitado com cacha alta")
    elif(escolha=='P'):
        print(funcionarios)
    elif(escolha=='S'):
        escolha_sair = str(input("Deseja sair do programa? Sim (S) ou não (N): ")).upper()
        if(escolha_sair=='S'):
            break