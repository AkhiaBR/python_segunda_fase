# Exercício 04
# Nome: Fernando Gonçalves

import mysql.connector # importa a função de import do conector mysql

conexao_banco = mysql.connector.connect( # especifica a conexão com o database determinado
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "hotel2"
)
cursor = conexao_banco.cursor()

def cadastrar():
    nome_cliente = str(input("Digite o nome do cliente: "))
    quarto = int(input("Digite o código do quarto à ser reservado: "))
    data_checkin = str(input("Digite a data do checkin (formato - YYYY-MM-DD): "))
    data_checkout = str(input("Digite a data do checkout (formato - YYYY-MM-DD): "))

    comando_sql = (f'INSERT INTO reservas (nome_cliente,quarto,data_checkin,data_checkout) VALUES ("{nome_cliente}",{quarto},"{data_checkin}","{data_checkout}")')
    cursor.execute(comando_sql)
    conexao_banco.commit()

def alterar():
    id_reserva = int(input("Digite o ID da reserva que deseja alterar: "))
    data_checkin = str(input("Digite a nova data do checkin (formato - YYYY-MM-DD): "))
    data_checkout = str(input("Digite a nova data do checkout (formato - YYYY-MM-DD): "))

    comando_sql = (f'UPDATE reservas SET data_checkin = "{data_checkin}", data_checkout = "{data_checkout}" WHERE id = {id_reserva}')
    cursor.execute(comando_sql)
    conexao_banco.commit()

def excluir():
    comando_sql = ('SELECT * FROM reservas')
    cursor.execute(comando_sql)
    db = cursor.fetchall()

    id_reserva = int(input("Forneça o ID da reserva que deseja excluir: "))
    
    for i in db:
        if(i[0] == id_reserva):
            comando_sql = (f'DELETE FROM reservas WHERE id = {id_reserva}')
            cursor.execute(comando_sql)
            conexao_banco.commit()

def pesquisar():
    comando_sql = ('SELECT * FROM reservas')
    cursor.execute(comando_sql)
    db = cursor.fetchall()

    op = int(input("Deseja pesquisar por NOME CLIENTE (1) ou QUARTO (2)?: "))

    if(op==1):
        nome = str(input("Digite o nome do cliente que deseja pesquisar: "))
        comando_sql = (f'SELECT * FROM reservas WHERE nome = "{nome}"')
        cursor.execute(comando_sql)
        result = cursor.fetchall() # retorna e salva em uma variável o que foi executado anteriormente
        print(result)
    elif(op==2):
        quarto = int(input("Digite o código do quarto que deseja pesquisar: "))
        comando_sql = (f'SELECT * FROM reservas WHERE quarto = "{quarto}"') 
        cursor.execute(comando_sql)
        result = cursor.fetchall() # retorna e salva em uma variável o que foi executado anteriormente
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