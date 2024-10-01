import mysql.connector # importa a função de import do conector mysql

conexao_banco = mysql.connector.connect( # especifica a conexão com o database
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "vendas"
)

cursor = conexao_banco.cursor() # define que conexao_banco é um objeto manipulável por comandos SQL

# CRUD (CREATE, READ, UPDATE, DELETE)

# CREATE 

nome = str(input("Digite o nome do produto: "))
valor = float(input("Digite o valor do produto: "))

comando_sql = (f'INSERT INTO produtos (nome_produto,valor_produto) VALUES ("{nome}",{valor})') # define o que vai ser colocado na tabela
cursor.execute(comando_sql) # executa as alterações, executando a variável cursor criada anteriormente
conexao_banco.commit() # commita as alterações no banco

# UPDATE

id_p = int(input("Digite o ID do produto que deseja alterar: "))
nome = str(input("Digite o novo nome do produto: "))

comando_sql = (f'UPDATE produtos SET nome_produto = "{nome}" WHERE id_produtos = {id_p}')
cursor.execute(comando_sql)
conexao_banco.commit()