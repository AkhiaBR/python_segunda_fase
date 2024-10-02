# questão 2 - Fernando Gonçalves / 2190

funcionarios = {}

while True:
    nome = str(input("Digite o nome do funcionário: "))
    salario = float(input("Digite o salário desse funcionário: "))
    funcionarios[nome] = salario
    op = str(input("Deseja continuar cadastrando funcionários? S/N: ")).upper().strip()

    if(op=="N"):
        break

valor = float(input("Digite o valor mínimo para a aplicação do aumento: "))

func_valor = dict(filter(lambda x: x[1]>valor,funcionarios.items())) # x[1] = posicao do salario na tupla: (nome, salario) 
func_aumento = dict(map(lambda x: (x[0], x[1]+(x[1]*15/100)),func_valor.items()))
for nome, salario in func_aumento.items(): # atualiza o dicionário
    funcionarios[nome] = salario
media_salario = sum(funcionarios.values())/len(funcionarios)

print(f"Lista de funcionários: {funcionarios}")
print(f"Média salarial dos funcionários: {media_salario}")
print(f"Maior salário: {max(funcionarios.values())}")
print(f"Menor salário: {min(funcionarios.values())}")