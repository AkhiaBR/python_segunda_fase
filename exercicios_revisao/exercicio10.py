# Exercício 10
# Nome: Fernando Gonçalves

print("MENU de Tipos de Combustíveis: ")
print("A - Álcool")
print("G - Gasolina")
print("---------------------------------------")

combustivel = str(input("Digite a sigla do combustível desejado (A) ou (G): ")).upper()
litro = float(input("Quantos litros desse combustível você deseja?: "))

if(combustivel=="A" and litro<=20):
    valor_bruto = litro*4.22
    valor_real = valor_bruto-(valor_bruto*0.03)
elif(combustivel=="A" and litro>20):
    valor_bruto = litro*4.22
    valor_real = valor_bruto-(valor_bruto*0.05)
elif(combustivel=="G" and litro<=20):
    valor_bruto = litro*5.65
    valor_real = valor_bruto-(valor_bruto*0.04)
elif(combustivel=="G" and litro>20):
    valor_bruto = litro*5.65
    valor_real = valor_bruto-(valor_bruto*0.06)

print("---------------------------------------")
print(f"O valor a ser pago será de {valor_real}")