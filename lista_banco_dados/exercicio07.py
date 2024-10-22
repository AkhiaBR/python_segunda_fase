# Exercício 01
# Nome: Fernando Gonçalves

import mysql.connector

conexao_banco = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "biblioteca"
)

cursor = conexao_banco.cursor()

def cadastrar():
    titulo = str(input("Digite o nome do livro: "))
    autor = str(input("Digite o nome do autor: "))
    ano_publicacao = int(input("Digite o ano em que o livro foi publidado: "))
    disponibilidade_input = str(input("O livro está disponível? Sim (S), não (N): ")).upper()

    if(disponibilidade_input=="S"):
        disponibilidade = True
    elif(disponibilidade_input=="N"):
        disponibilidade = False

    comando_sql = (f'INSERT INTO livros (titulo,autor,ano_publicacao,disponibilidade) VALUES ("{titulo}","{autor}",{ano_publicacao},"{disponibilidade}")')
    cursor.execute(comando_sql)
    conexao_banco.commit()

def alterar():
    comando_sql = ('SELECT * FROM livros')
    cursor.execute(comando_sql)
    db = cursor.fetchall()

    id_livro = int(input("Digite o ID do livro que deseja alterar: "))

    for i in db: 
        if(id_livro==i[0]):
            disponibilidade_input = str(input("O livro está disponível? Sim (S), não (N): ")).upper()

            if(disponibilidade_input=="S"):
                disponibilidade = True
            elif(disponibilidade_input=="N"):
                disponibilidade = False

    comando_sql = (f'UPDATE livros SET disponibilidade = "{disponibilidade}" WHERE id = {id_livro}')
    cursor.execute(comando_sql)
    conexao_banco.commit()

def excluir():
    id_livro = int(input("Digite o ID do livro que deseja alterar: "))

    comando_sql = (f'DELETE FROM livros WHERE id = {id_livro}')
    cursor.execute(comando_sql)
    conexao_banco.commit()

def pesquisar():
    comando_sql = ('SELECT * FROM livros')
    cursor.execute(comando_sql)
    db = cursor.fetchall()

    op = str(input("Deseja filtrar por título (T), ou autor (A): ")).upper()

    for i in db:
        if(op=="T"):
            titulo_pesquisa = str(input("Digite o título da obra: "))

            if(i[1]==titulo_pesquisa):
                comando_sql = (f'SELECT * FROM livros WHERE titulo = "{titulo_pesquisa}"')
                cursor.execute(comando_sql)
                result = cursor.fetchall()
                print(result)
                
        elif(op=="A"):
            autor_pesquisa = str(input("Digite o autor da obra: "))

            if(i[2]==autor_pesquisa):
                comando_sql = (f'SELECT * FROM livros WHERE autor = "{autor_pesquisa}"')
                cursor.execute(comando_sql)
                result = cursor.fetchall()
                print(result)

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