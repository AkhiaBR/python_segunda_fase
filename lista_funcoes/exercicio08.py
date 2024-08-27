# Exercício 08
# Nome: Fernando Gonçalves

import random
numero_aleatorio = random.randint(1,100) # o numero aleatorio deve estar fora do loop para que ele nao seja gerado repetidamente

while(True):
    numero_chute = int(input("Tente acertar o número aleatório digitando valores de 1 a 100: "))

    if(numero_chute<1 or numero_chute>100):
        print("Valor errado, digite novamente")
    elif(numero_chute!=numero_aleatorio):
        print("Parece que você chutou errado, tente novamente")
    elif(numero_chute==numero_aleatorio):
        print(f"Parabéns! Você acertou o número aleatório. O número aleatório era: {numero_aleatorio}")
        break