# questão 1 - Fernando Gonçalves / 2190

tupla_times = (
    "Botafogo", "Fortaleza", "Flamengo", "Palmeiras", "São Paulo", "Cruzeiro", "Bahia", "Athletico-PR", "Atlético-MG", "Vasco", "Bragantino",
    "Juventude", "Grêmio", "Criciúma", "Internacional", "Vitória", "Corinthians", "Fluminense", "Cuiabá", "Atlético-GO"
)

primeiro_cinco = tupla_times[:5]
ultimo_quatro = tupla_times[-4:]
ordem_alfa = sorted(tupla_times)
posicao_corin = tupla_times.index("Corinthians")+1
print(f"Primeiros cinco colocados: {primeiro_cinco}")
print(f"Últimos quatro colocados: {ultimo_quatro}")
print(f"Tupla em ordem alfabética: {ordem_alfa}")
print(f"Qual a posição do Corinthians na lista: {posicao_corin}")