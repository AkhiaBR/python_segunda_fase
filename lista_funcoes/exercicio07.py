# Exercício 07
# Nome: Fernando Gonçalves

import math

def calculo_hipotenusa(co,ca):
    hipotenusa = math.hypot(co,ca) # a funcao math.hypot faz o calculo automatico da resolucao da hipotenusa com a biblioteca math
    return(hipotenusa) 

print("__________________________")
cateto_oposto = float(input("Digite o valor do cateto oposto: "))
cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))
hipotenusa = calculo_hipotenusa(cateto_oposto,cateto_adjacente)
print(f"O valor da hipotenusa é: {hipotenusa}")