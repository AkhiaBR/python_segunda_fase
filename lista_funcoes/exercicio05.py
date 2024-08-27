# Exercício 05
# Nome: Fernando Gonçalves

from datetime import *
from time import *

reserva = {}

def destinos():
    lugares = {1:"Rio de Janeiro", 2:"São Paulo", 3:"Porto Alegre", 4:"Florianópolis"}
    print(lugares)
    escolha_lugar = int(input("Digite o número do destino desejado: "))
    reserva["destino"] = escolha_lugar

def datas():
    print("Insira valores inteiros")
    dia = int(input("Digite o dia da viagem: "))
    mes = int(input("Digite o mês da viagem: "))
    ano = int(input("Digite o ano da viagem: "))
    data = (f"{ano}/{mes}/{dia}")
    reserva["data"] = data


def num_passageiros():
    numero = int(input("Digite o número de passageiros na viagem: "))
    reserva["numero de passageiros"] = numero


while(True):
    print("_____________________")
    print("1- Reservar Passagem")
    print("2- Sair do Programa")
    print("_____________________")
    escolha = int(input("Digite o número da opção do menu desejada: "))

    if(escolha==1):
        destinos()
        datas()
        num_passageiros()
        print(f"Sua reserva está da seguinte forma: {reserva}")
    elif(escolha==2):
        break
