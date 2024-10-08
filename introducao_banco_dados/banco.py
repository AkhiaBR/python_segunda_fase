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

comando_sql = ('SELECT * FROM produtos')
cursor.execute(comando_sql)
db = cursor.fetchall() # busca - fetch - e armazena os dados da tabela em uma variável - o fetch precisa armazenar os dados em algum lugar

id_p = int(input("Digite o ID do produto que deseja alterar: "))
nome = str(input("Digite o novo nome do produto: "))

for i in db: # para cada tupla dentro de db
    if(i[0] == id_p): # se o ID - posicao 0 da tupla for igual ao ID digitado: 
        print("ERRO: Produto já cadastrado. Tente novamente...")

comando_sql = (f'UPDATE produtos SET nome_produto = "{nome}" WHERE id_produtos = {id_p}')
cursor.execute(comando_sql)
conexao_banco.commit()

# DELETE 

id_p = int(input("Digite o ID do produto que deseja excluir: "))

comando_sql = (f'DELETE FROM produtos WHERE id_produtos = {id_p}')
cursor.execute(comando_sql)
conexao_banco.commit()

# READ

comando_sql = ('SELECT * FROM produtos')
cursor.execute(comando_sql)
db = cursor.fetchall() # busca - fetch - e armazena os dados da tabela em uma variável - o fetch precisa armazenar os dados em algum lugar
print(f"Terceiro item da tabela: {db[2]}") # printa o terceiro item da tabela - o segundo item da tupla
print(f"ID do segundo item da tabela: {db[1][0]}") # printa o ID do segundo item da tabela
print(f"Nome do terceiro item da tabela: {db[2][1]}") # printa o nome do terceiro item da tabela
print(f"Valor do primeiro item da tabela: {db[0][2]}") # printa o valor do primeiro item da tabela

for i in db: # para os itens - cada tupla da lista 
    print(f"ID: {i[0]}, Produto: {i[1]}, Valor: {i[2]}")