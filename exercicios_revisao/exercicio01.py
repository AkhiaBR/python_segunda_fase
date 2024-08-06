# Exercício 01
# Nome: Fernando Gonçalves

ganho_hora = float(input("Quanto você ganha por hora?: "))
mes_hora = float(input("Digite a quantidade de horas trabalhadas por mês: "))
salario_bruto = (ganho_hora*mes_hora)
salario_real = salario_bruto-((salario_bruto*0.11)+(salario_bruto*0.08)+(salario_bruto*0.05))

print(f"Seu salário bruto é: {salario_bruto}")
print(f"Já seu salário real é de {salario_real}")