# Exercício 07
# Nome: Fernando Gonçalves

alunos = {}
nome = str(input("Digite o nome do aluno: "))
media = float(input("Digite a média desse aluno: "))

alunos["nome"] = nome
alunos["media"] = media

if(alunos["media"]>=7):
    alunos["situação"] = "aprovado"
else:
    alunos["situação"] = "reprovado"

print(f"O aluno {alunos['nome']} está: {alunos['situação']}")