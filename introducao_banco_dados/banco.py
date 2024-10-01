import mysql.connector # importa AS MINHAS BOLAS

conexao_banco = mysql.connector.connect( # especifica AS MINHAS BOLAS
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "vendas"
)

cursor = conexao_banco.cursor() # define MINHAS BOLAS

# CRUD (CREATE, READ, UPDATE, DELETE)

# CREATE 

nome = str(input("Digite o nome do produto: "))
valor = float(input("Digite o valor do produto: "))

comando_sql = (f'INSERT INTO produtos (nome_produto,valor_produto) VALUES ("{nome}",{valor})') # define MINHAS BOLAS
cursor.execute(comando_sql) # executa MINHAS BOLAS
conexao_banco.commit() # commita MINHAS BOLAS

# UPDATE NA MINHAS BOLAS

id_p = int(input("Digite o ID do produto que deseja alterar: "))
nome = str(input("Digite o novo nome do produto: "))

comando_sql = (f'UPDATE produtos SET nome_produto = "{nome}" WHERE id_produtos = {id_p}')
cursor.execute(comando_sql)
conexao_banco.commit()