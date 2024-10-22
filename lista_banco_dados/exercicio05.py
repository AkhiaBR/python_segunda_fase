# Exercício 05
# Nome: Fernando Gonçalves

import mysql.connector

conexao_banco = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "escola"
)

cursor = conexao_banco.cursor()

def cadastrar():
    comando_sql = ('SELECT * FROM cadastros')
    cursor.execute(comando_sql)
    db = cursor.fetchall()

    id_aluno = int(input("Digite o ID do aluno que deseja cadastrar: "))

    for i in db:
        if(i[0]==id_aluno):
            print("ERRO: Aluno já existente. Tente novamente...")

    else: # else depois do for porque depois de rodar todas as probabilidades do laço, o else será executado (o laço é rodado para cada linha da tupla)
        nome = str(input("Digite o nome do aluno que deseja cadastrar: "))
        curso = str(input("Digite o curso em que ele faz parte: "))
        ano_ingresso = int(input("Digite o ano de ingresso do aluno: "))

        comando_sql = (f'INSERT INTO cadastros (id, nome, curso, ano_ingresso) VALUES ({id_aluno},"{nome}","{curso}",{ano_ingresso})')
        cursor.execute(comando_sql)
        conexao_banco.commit()

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