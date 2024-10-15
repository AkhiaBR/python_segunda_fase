# Exercício 01
# Nome: Fernando Gonçalves

import mysql.connector # importa a função de import do conector mysql

conexao_banco = mysql.connector.connect( # especifica a conexão com o database determinado
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "loja"
)
cursor = conexao_banco.cursor()

def cadastrar():
    nome = str(input("Digite o nome do produto: "))
    categoria = str(input("Digite a categoria em que o produto se enquadra: "))
    quantidade = int(input("Digite a quantidade do produto no inventário: "))

    comando_sql = (f'INSERT INTO produtos (nome,categoria,quantidade) VALUES ("{nome}","{categoria}",{quantidade})')
    cursor.execute(comando_sql)
    conexao_banco.commit()

def alterar():
    id_produto = int(input("Digite o ID do produto que deseja alterar: "))
    quantidade = int(input("Digite a nova quantiade do produto: "))

    comando_sql = (f'UPDATE produtos SET quantidade = "{quantidade}" WHERE id = {id_produto}')
    cursor.execute(comando_sql)
    conexao_banco.commit()

def excluir():
    comando_sql = ('SELECT * FROM produtos')
    cursor.execute(comando_sql)
    db = cursor.fetchall()

    id_produto = int(input("Forneça o ID do produto que deseja excluir: "))
    
    for i in db:
        if(i[0] == id_produto):
            comando_sql = (f'DELETE FROM produtos WHERE id = {id_produto}')
            cursor.execute(comando_sql)
            conexao_banco.commit()

def pesquisar():
    comando_sql = ('SELECT * FROM produtos')
    cursor.execute(comando_sql)
    db = cursor.fetchall()

    print(f"Todos os produtos em ordem numérica: {sorted(db)}")


while True:
    print("====================")
    print("1- Cadastrar")
    print("2- Alterar")
    print("3- Excluir")
    print("4- Pesquisar")
    print("5- Sair")
    print("====================")
    op = int(input("Digite o número referente à opção desejada no menu: "))

    if(op==1):
        cadastrar()
    elif(op==2):
        alterar()
    elif(op==3):
        excluir()
    elif(op==4):
        pesquisar()
    elif(op==5):
        break
    else:
        print("ERRO: Valor digitado inválido. Tente novamente...")