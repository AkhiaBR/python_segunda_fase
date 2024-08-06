# Exercício 08
# Nome: Fernando Gonçalves

candidato01 = 0
candidato02 = 0
candidato03 = 0

numero_eleitores = int(input("Quantas pessoas irão votar nos candidatos?: "))
total_votos = 0

while(total_votos<numero_eleitores):
    print("Cadidatos possíveis: ")
    print("1- Roberto")
    print("2- Cláudio")
    print("3- Estácia")
    print("---------------------------")

    votos = int(input("Digite o número do candidato que deseja votar: "))

    print("---------------------------")

    if(votos==1):
        candidato01+=1
        total_votos+=1
    elif(votos==2):
        candidato02+=1
        total_votos+=1
    elif(votos==3):
        candidato03+=1
        total_votos+=1

print(f"Número total de votos do candidato Roberto: {candidato01}")
print(f"Número total de votos do candidato Cláudio: {candidato02}")
print(f"Número total de votos do candidato Estácia: {candidato03}")
