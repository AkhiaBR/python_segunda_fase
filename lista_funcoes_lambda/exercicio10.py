# Exercício 10
# Nome: Fernando Gonçalves

temperaturas_celsius = [0,403,50,60]

temperatura_convertida = list(map(lambda x : (x*9/5)+32,temperaturas_celsius))
print(f"A lista em Celsius convertida é: {temperatura_convertida}")