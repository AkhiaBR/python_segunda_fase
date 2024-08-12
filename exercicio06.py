# Exercício 06
# Nome: Fernando Gonçalves

tupla_palavras = ("reino", "arvore", "escola", "pao", "sphynx")

for palavra in tupla_palavras: # para todas as palavras em tupla_palavras
    vogais = [] 
    for letra in palavra: # para todas as letras em palavras
        if(letra in "aeiou"):
            vogais.append(letra)
    
    if(vogais):
        print(f"A palavra {palavra} possui as vogais: {vogais}")
    else:
        print(f"A palavra {palavra} não possui nenhuma vogal")
