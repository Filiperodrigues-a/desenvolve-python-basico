idade = int(input("Informe sua idade:"))
partidas = input("Já jogou pelo menos 3 jogos de tabuleiro?")
vitorias = int(input("Quantos jogos já venceu?"))
apto_idade = idade>=16 and idade<=18
apto_partida = partidas == 'True'
apto_vitorias = vitorias>=1
apto = apto_idade and apto_partida and apto_vitorias

print(f"Apto para ingressar no clube de jogos de tabuleiro:{apto}")