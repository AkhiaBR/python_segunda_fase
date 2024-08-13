# Exercício 12
# Nome: Fernando Gonçalves

carros = { 1 : [ "fiat", "palio", "ano 2022", "prata"], 
           2 : [ "ford", "fiesta", "ano 2023", "branca"],
           3 : [ "honda", "fit", "ano 2024", "preta"], }
estado = True

while(estado==True):
    print("-----------------------")
    print("1- Cadastrar")
    print("2- Excluir")
    print("3- Pesquisar")
    print("4- Sair")
    print("-----------------------")
    escolha = int(input("Digite o número da opção desejada: "))

    if(escolha==1):
        cod_carro = int(input("Digite o código do carro que deseja cadastar: "))
        if(cod_carro in carros.keys()): # Se a chave já existe, erro
            print("O código do carro que você deseja cadastrar já está em uso")
        else:
            cod_carro = len(carros)+1 # Adiciona uma nova casa para o dicionário
            marca = str(input("Digite a marca desse carro: "))
            modelo = str(input("Digite o modelo do carro: "))
            ano = int(input("Digite o ano desse carro: "))
            cor = str(input("Digite a cor do carro: "))
            carros[cod_carro] = [marca, modelo, ano, cor]
    elif(escolha==2):
        cod_carro = int(input("Digite o código do carro que deseja remover: "))
        if(cod_carro in carros.keys()):
            del carros[cod_carro]
            print("Carro deletado com sucesso!")
        else:
            print("Não há nenhum carro com este código no programa")
    elif(escolha==3):
        print(carros)
    elif(escolha==4):
        sair_escolha = str(input("Deseja sair do programa? Sim (S) ou não (N): ")).upper()
        if(sair_escolha=='S'):
            break