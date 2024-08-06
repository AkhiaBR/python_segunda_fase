# Exercício 09
# Nome: Fernando Gonçalves

contador = 0
altura_homens = []
altura_mulheres = []
num_pessoas = 0
num_homens = 0
num_mulheres = 0


while(contador<50):
    sexo = str(input("Digite o seu sexo (M) masculino e (S) feminino: ")).upper()
    altura = float(input("Digite o valor de sua altura: "))

    if(sexo=="M"):
        contador+=1
        num_homens+=1
        num_pessoas+=1
        altura_homens.append(altura)
    elif(sexo=="F"):
        contador+=1
        num_mulheres+=1
        num_pessoas+=1
        altura_mulheres.append(altura)
    
print(f"Altura do maior homem: {max(altura_homens)}, altura da maior mulher: {max(altura_mulheres)}")
print(f"Altura do menor homem: {min(altura_homens)}, altura da menor mulher: {min(altura_mulheres)}")
print(f"Média de altura das mulheres: {sum(altura_mulheres)/num_mulheres}")
print(f"Número de homens: {num_homens}")
print(f"Porcentagem de homens: {(num_homens/num_pessoas)*100}, porcentagem de mulheres: {(num_mulheres/num_pessoas)*100}")

