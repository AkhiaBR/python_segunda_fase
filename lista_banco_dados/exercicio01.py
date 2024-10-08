# Exercício 01
# Nome: Fernando Gonçalves

import mysql.connector # importa a função de import do conector mysql

conexao_banco = mysql.connector.connect( # especifica a conexão com o database
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
        if(i[1],i[2],i[3],i[4] == marca,modelo,ano,cor):
            print("ERRO: Veículo já cadastrado. Tente novamente...")
        else:
            comando_sql = (f'INSERT INTO carros (marca,modelo,ano,cor) VALUES ("{marca}","{modelo}",{ano},"{cor}")')
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
    # elif(op==2):
    #     excluir()
    # elif(op==3):
    #     pesquisar()
    # elif(op==4):
    #     break
    else:
        print("ERRO: Valor digitado inválido. Tente novamente...")