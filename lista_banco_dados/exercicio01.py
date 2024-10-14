# Exercício 01
# Nome: Fernando Gonçalves

import mysql.connector # importa a função de import do conector mysql

conexao_banco = mysql.connector.connect( # especifica a conexão com o database determinado
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "concessionaria"
)
cursor = conexao_banco.cursor()

def cadastrar():
    comando_sql = ('SELECT * FROM carros')
    cursor.execute(comando_sql)
    db = cursor.fetchall()

    marca = str(input("Digite a marca do veículo: "))
    modelo = str(input("Digite modelo do veículo: "))
    ano = int(input("Digite o ano do veículo: "))
    cor = str(input("Digite a cor do veículo: "))

    for i in db:
        if(i[1],i[2],i[3] == marca,modelo,ano):
            print("ERRO: Veículo já cadastrado. Tente novamente...")
        else:
            comando_sql = (f'INSERT INTO carros (marca,modelo,ano,cor) VALUES ("{marca}","{modelo}",{ano},"{cor}")')
            cursor.execute(comando_sql)
            conexao_banco.commit()

def excluir():
    comando_sql = ('SELECT * FROM carros')
    cursor.execute(comando_sql)
    db = cursor.fetchall()

    id_carro = int(input("Forneça o ID do carro que deseja excluir: "))
    
    for i in db:
        if(i[0] == id_carro):
            comando_sql = (f'DELETE FROM carros WHERE id = {id_carro}')
            cursor.execute(comando_sql)
            conexao_banco.commit()
        else:
            print("ERRO: ID não existente. Tente novamente...")

def pesquisar():
    comando_sql = ('SELECT * FROM carros')
    cursor.execute(comando_sql)
    db = cursor.fetchall()

    op = int(input("Deseja pesquisar por MARCA (1), MODELO (2) ou ANO (3)?:")).strip()

    if(op==1):
        marca = str(input("Digite a marca que deseja pesquisar: "))
        comando_sql = (f'SELECT * FROM carros WHERE marca = "{marca}"')
        cursor.execute(comando_sql)
        conexao_banco.commit()
    elif(op==2):
        modelo = str(input("Digite o modelo que deseja pesquisar: "))
        comando_sql = (f'SELECT * FROM carros WHERE modelo = "{modelo}"') 
        cursor.execute(comando_sql)
        conexao_banco.commit()
    elif(op==3):
        ano = int(input("Digite o ano que deseja pesquisar: "))
        comando_sql = (f'SELECT * FROM carros WHERE ano = {ano}') 
        cursor.execute(comando_sql)
        conexao_banco.commit()
while True:
    print("====================")
    print("1- Cadastrar")
    print("2- Excluir")
    print("3- Pesquisar")
    print("4- Sair")
    print("====================")
    op = int(input("Digite o número referente à opção desejada no menu: "))

    if(op==1):
        cadastrar()
    elif(op==2):
        excluir()
    elif(op==3):
        pesquisar()
    elif(op==4):
        break
    else:
        print("ERRO: Valor digitado inválido. Tente novamente...")