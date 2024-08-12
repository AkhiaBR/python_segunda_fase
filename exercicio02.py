# Exercício 02
# Nome: Fernando Gonçalves

tupla_jogadores = ("Rivaldo", "Brazão", "Tigrão", "Cachorro", "Falcão", "Rato", "Gatão", "Matador", "Lobão", "Jaguar", "Voador", "Touro", "Águia", "Morcego", "Furacão", "Raio", "Ciclone", "Saci", "Dinamite", "Bolado")
tupla_times = (("Flamengo", "Corinthians", "Palmeiras", "Santos", "Chapecoense", "Grêmio", "Cruzeiro", "Atlético Mineiro", "Internacional", "Fluminense", "Vasco da Gama"))
times_alfabetico = sorted(tupla_times)

print(f"Cinco primeiros ganhadores: {tupla_jogadores[:5]}") 
print("-------------------------------------------------------------------------------")
print(f"Quatro últimos ganhadores: {tupla_jogadores[-4:]}")
print("-------------------------------------------------------------------------------")
print(f"Times brasileiros em ordem alfabética: {times_alfabetico}")
print("-------------------------------------------------------------------------------")
print(f"Posição do Chapecoense: ",{tupla_times.index("Chapecoense")+1})