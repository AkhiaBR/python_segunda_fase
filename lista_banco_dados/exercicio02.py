# Exercício 01
# Nome: Fernando Gonçalves

import mysql.connector # importa a função de import do conector mysql

conexao_banco = mysql.connector.connect( # especifica a conexão com o database determinado
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "empresa"
)
cursor = conexao_banco.cursor()

def cadastrar():
    nome = str(input("Digite o nome do funcionário: "))
    cargo = str(input("Digite o cargo do funcionário: "))

    comando_sql = (f'INSERT INTO funcionarios (nome,cargo) VALUES ("{nome}","{cargo}")')
    cursor.execute(comando_sql)
    conexao_banco.commit()

def alterar():
    id_funcionario = int(input("Digite o ID do funcionáio que deseja alterar: "))
    cargo = str(input("Digite o novo cargo do funcionário: "))

    comando_sql = (f'UPDATE funcionarios SET cargo = "{cargo}" WHERE id = {id_funcionario}')
    cursor.execute(comando_sql)
    conexao_banco.commit()

def excluir():
    comando_sql = ('SELECT * FROM funcionarios')
    cursor.execute(comando_sql)
    db = cursor.fetchall()

    id_funcionario = int(input("Forneça o ID do funcionário que deseja excluir: "))
    
    for i in db:
        if(i[0] == id_funcionario):
            comando_sql = (f'DELETE FROM funcionarios WHERE id = {id_funcionario}')
            cursor.execute(comando_sql)
            conexao_banco.commit()

def pesquisar():
    op = int(input("Deseja filtrar por NOME (1) ou CARGO (2)?: "))

    if(op==1):
        nome = str(input("Digite o nome que deseja filtrar: "))
        comando_sql = (f'SELECT * FROM funcionarios WHERE nome = "{nome}"')

        cursor.execute(comando_sql)
        result = cursor.fetchall() # retorna e salva em uma variável o que foi executado anteriormente
        print(result)
        print(f"Total de funcionários cadastrados: {total_funcionarios}")
    elif(op==2):
        comando_sql = ('SELECT * FROM funcionarios')
        cursor.execute(comando_sql)
        db = cursor.fetchall()

        cargo = str(input("Digite o cargo que deseja filrar: "))
        comando_sql = (f'SELECT * FROM funcionarios WHERE cargo = "{cargo}"')

        for i in db:
            total_funcionarios = len(db)

        cursor.execute(comando_sql)
        result = cursor.fetchall() # retorna e salva em uma variável o que foi executado anteriormente
        print(result)
        print(f"Total de funcionários cadastrados: {total_funcionarios}")


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